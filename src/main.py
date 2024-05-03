from src.financial_operations.financial_manager import FinancialManager
from utils.decorators import choice_decorator
from interface.menus import Menu


@choice_decorator(Menu.main_menu)
def main(choice: int):
    if choice == 1:
        FinancialManager.check_balance()
    elif choice == 2:
        FinancialManager.add_transaction()
    elif choice == 3:
        FinancialManager.change_transaction()
    elif choice == 4:
        FinancialManager.find_transaction()
    elif choice == 0:
        exit()


if __name__ == '__main__':
    while True:
        main()

