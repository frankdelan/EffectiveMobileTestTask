import csv
import pytest

from src.financial_operations.financial_manager import FinancialManager
from src.utils.file_operations import CSVController
from src.config import DATABASE_PATH


@pytest.fixture(autouse=True)
def setup_file():
    """
    Очистка файла
    """
    with open(DATABASE_PATH, 'w', encoding='utf-8'): pass
    yield
    with open(DATABASE_PATH, 'w', encoding='utf-8'): pass


@pytest.fixture()
def fill_file() -> int:
    """
    Заполнение файла тестовыми данными и возврат баланса
    """
    test_data: list[list[str]] = [['2024-05-11', 'Доход', '1000', 'Test1'],
                                  ['2024-05-11', 'Доход', '2500', 'Test2'],
                                  ['2024-05-11', 'Расход', '3500', 'Test3']]
    with open(DATABASE_PATH, 'w', encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(test_data)

    return sum(list(map(lambda x: int(x[2]) if x[1] == 'Доход' else -int(x[2]), test_data)))


class TestCalculator:
    def test_check_balance(self, capsys, fill_file):
        FinancialManager.check_balance()
        balance = capsys.readouterr().out
        assert balance == f'Текущий баланс: {fill_file}\n'

    @pytest.mark.parametrize("category, category_name, money, description",
                             [('1', "Доход", '1000', "Test"), ('2', "Расход", '1800', "New test")])
    def test_transaction_add(self, mocker, category, category_name, money, description):
        mocker.patch("builtins.input", side_effect=[category, money, description])
        FinancialManager.add_transaction()

        with open(DATABASE_PATH, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            transactions = list(csv_reader)

        assert len(transactions) == 1
        assert transactions[0][1] == category_name
        assert transactions[0][2] == money
        assert transactions[0][3] == description

    @pytest.mark.parametrize("transaction_number, category, new_data",
                             [(0, 3, "8000"), (1, 4, "Описание"), (2, 1, "2024-09-09")])
    @pytest.mark.usefixtures("fill_file")
    def test_change_transaction(self, mocker, transaction_number, category, new_data):
        mocker.patch("builtins.input", side_effect=[0, transaction_number, category, new_data])
        FinancialManager.change_transaction()
        with open(DATABASE_PATH, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            transactions = list(csv_reader)
        assert transactions[transaction_number][category - 1] == new_data

    @pytest.mark.parametrize("search_field, value, result_count",
                             [(3, '2500', 1), (4, 'Test2', 1)])
    @pytest.mark.usefixtures("fill_file")
    def test_find_transaction(self, mocker, search_field, value, result_count):
        mocker.patch("builtins.input", side_effect=[search_field, value])
        FinancialManager.find_transaction()
        records: list = CSVController.search_info(search_field - 1, value)
        assert len(records) == result_count
