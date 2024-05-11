from datetime import datetime

from utils.file_operations import CSVController
from interface.menus import Menu
from utils.decorators import choice_decorator


class TransactionInputValidator:
    @staticmethod
    def validate_date_format(date_string: str) -> str | None:
        """
        Статический метод для проверки корректного ввода даты.
        Возвращает None или str
        """
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return date_string
        except ValueError:
            print('Некорректный формат даты.')
            return

    @staticmethod
    def validate_category(category: str) -> str | None:
        """
        Статический метод для проверки корректного ввода категории.
        Возвращает None или str
        """
        if category == 'Доход' or category == 'Расход':
            return category
        else:
            print('Неизвестная категория.')
            return

    @staticmethod
    def validate_summary(cash: str) -> str | None:
        """
        Статический метод для проверки корректного ввода суммы.
        Возвращает None или int
        """
        try:
            int(cash)
            return cash
        except ValueError:
            print('Некорректный ввод суммы.')
            return


class TransactionHandler:
    field_validators = {
        0: TransactionInputValidator.validate_date_format,
        1: TransactionInputValidator.validate_category,
        2: TransactionInputValidator.validate_summary,
        3: lambda x: x
    }

    @staticmethod
    @choice_decorator(lambda: print('Введите сумму денег:'))
    def get_money_count(cash: int) -> None | int:
        """
        Статический метод для получения суммы денег при создании транзакции.
        Возвращает None или int
        """
        return cash

    @staticmethod
    def get_description() -> str:
        """
        Статический метод для получения описания при создании транзакции.
        Возвращает str.
        """
        print('Введите описание транзакции:')
        description: str = input()
        return description

    @staticmethod
    def create_transaction(status: str) -> None:
        """
        Статический метод для создания транзакции.
        Возвращает None.
        """
        money: int = TransactionHandler.get_money_count()
        if money is None:
            return
        description: str = TransactionHandler.get_description()
        try:
            CSVController.add_info_to_file([datetime.now().date(), status, money, description])
        except Exception:
            print('Транзакция не была создана.')
            return
        print('Транзакция успешно создана!')

    @staticmethod
    def collect_search_data(field: int) -> None:
        """
        Статический метод для получения данных по транзакции для поиска.
        Возвращает None.
        """
        print('Введите данные для поиска:\n')
        Menu.transaction_data_formats()
        data: str = input()
        found_transaction: list = CSVController.search_info(field, data)
        if found_transaction:
            print(f'Найдено {len(found_transaction)} записей/записи.')
            for item in found_transaction:
                print('|'.join(item))
        else:
            print('Записи не найдены.')
            return

    @staticmethod
    def display_transactions_by_page() -> int:
        """
        Статический метод для отображения транзакций по странице(pagination).
        Возвращает int, как количество транзакций.
        """
        offset: int = 0
        limit: int = 3
        transactions_list: list = CSVController.get_all_transactions()
        while (offset + limit) < len(transactions_list) + limit:
            if transactions_list:
                for item in transactions_list[offset: offset + limit]:
                    print('|'.join(item))
            print('\n\nEnter - следующая страницы\n'
                  'Закончить просмотр - 0')
            button: str = input()
            if button == '0':
                return len(transactions_list)
            else:
                offset += limit
        return len(transactions_list)

    @staticmethod
    def get_new_info(row_number: int, field_number: int) -> None:
        """
        Статический метод для получения и проверки новых данных при изменении транзакции.
        Возвращает None.
        """
        print('Введите новые данные')
        Menu.transaction_data_formats()
        new_data: str = input()

        validator = TransactionHandler.field_validators.get(field_number)
        valid_data: str | None = validator(new_data)

        if valid_data:
            try:
                CSVController.update_csv_cell(row_number, field_number, valid_data)
            except Exception as e:
                print(f'Произошла ошибка - {e}')
                return
            else:
                print('Запись успешна изменена!')
        else:
            return

    @staticmethod
    @choice_decorator(Menu.change_transaction_menu)
    def update_transaction_data(field_id: int, transaction_number: int) -> None:
        """
        Статический метод для изменения существующей транзакции.
        Возвращает None.
        """
        if field_id in [1, 2, 3, 4]:
            TransactionHandler.get_new_info(transaction_number, field_id - 1)
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")
            return
