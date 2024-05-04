import csv

# working directory - /src/
FILEPATH: str = 'history.csv'


class CSVController:
    @staticmethod
    def get_user_balance() -> int:
        """
        Статический метод для расчета и возврата баланса пользователя.
        Возвращает число с плавающей запятой, представляющее баланс пользователя.
        """
        with open(FILEPATH, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            balance: int = 0

            for row in csv_reader:
                if row[1] == 'Доход':
                    balance += int(row[2])
                else:
                    balance -= int(row[2])
            return balance

    @staticmethod
    def search_info(field: int, data: str) -> list[str]:
        """
        Статический метод для поиска транзакций по параметру.
        Возвращает список с данными о транзакциях либо пустой список.
        """
        with open(FILEPATH, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            transactions: list[str] = []

            for idx, row in enumerate(csv_reader):
                if row[field] == data or data in row[field]:
                    transactions.append([f'{idx}'] + row)
            return transactions

    @staticmethod
    def add_info_to_file(data: list[str | int]) -> None:
        """
        Статический метод для добавления данных в файл.
        Возвращает None.
        """
        with open(FILEPATH, 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(data)

    @staticmethod
    def update_csv_cell(row_index: int, column_index: int, new_value: str) -> None:
        """
        Статический метод для изменения записей в файле.
        Возвращает None.
        """
        with open(FILEPATH, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = list(csv_reader)

        rows[row_index][column_index] = new_value

        with open(FILEPATH, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(rows)

    @staticmethod
    def get_all_transactions() -> list[str]:
        """
        Статический метод, возвращающий список со всеми транзакциями.
        """
        with open(FILEPATH, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            transactions: list[str] = []

            for idx, row in enumerate(csv_reader):
                transactions.append([f'{idx}'] + row)
            return transactions
