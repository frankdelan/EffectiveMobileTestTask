from src.utils.file_operations import CSVController
from src.financial_operations.transaction_manager import TransactionHandler
from src.interface.menus import Menu
from src.utils.decorators import choice_decorator


class FinancialManager:
    @staticmethod
    def check_balance() -> None:
        """
        Статический метод выводящий в консоль баланс пользователя.
        Возвращает None.
        """
        balance: float = CSVController.get_user_balance()
        print(f'Текущий баланс: {balance}')

    @staticmethod
    @choice_decorator(Menu.add_transaction_menu)
    def add_transaction(category_id: int) -> None:
        """
        Статический метод для добавления новой транзакции.
        Возвращает None.
        """
        if category_id == 1:
            TransactionHandler.create_transaction('Доход')
        elif category_id == 2:
            TransactionHandler.create_transaction('Расход')
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")
            return

    @staticmethod
    def change_transaction() -> None:
        """
        Статический метод для изменения транзакции.
        Вовзаращет None
        """
        transaction_count: int = TransactionHandler.display_transactions_by_page()
        print('Введите номер транзакции, которую хотите изменить.')
        try:
            transaction_number: int = int(input())
        except ValueError:
            print('Некорректный ввод.')
            return
        else:
            if transaction_number < transaction_count:
                TransactionHandler.update_transaction_data(transaction_number)
            else:
                print(f"Некорректный выбор. Всего транзакций {transaction_count}.")

    @staticmethod
    @choice_decorator(Menu.find_transaction_menu)
    def find_transaction(field_id: int) -> None:
        """
        Статический метод для поиска транзакции по параметру.
        Возвращает None.
        """
        if field_id in [1, 2, 3, 4]:
            return TransactionHandler.collect_search_data(field_id - 1)
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2, 3 или 4")
            return
