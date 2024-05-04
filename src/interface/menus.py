class Menu:
    @staticmethod
    def main_menu() -> None:
        print('\n\t-------Меню-------')
        print('1. Баланс счёта\n'
              '2. Добавить транзакцию\n'
              '3. Изменить данные о транзакции\n'
              '4. Найти транзакцию\n'
              '0. Закрыть')

    @staticmethod
    def add_transaction_menu() -> None:
        print('Категория:')
        print('1. Доход\n'
              '2. Расход')

    @staticmethod
    def find_transaction_menu() -> None:
        print('Поиск по:')
        print('1. Дате\n'
              '2. Категории\n'
              '3. Сумме\n'
              '4. Описание')

    @staticmethod
    def change_transaction_menu() -> None:
        print('Какое поле вы хотите изменить?')
        print('1. Дата\n'
              '2. Категория\n'
              '3. Сумма\n'
              '4. Описание')

    @staticmethod
    def transaction_data_formats() -> None:
        print('[Формат даты - (YYYY-MM-DD)]\n'
              '[Формат категории - ("Доход"/"Расход")]\n'
              '[Формат суммы - целочисленный]\n'
              '[Формат описания - текст]')
