from typing import Callable


def choice_decorator(menu: Callable):
    def decorator_func(func):
        def wrapper(*args, **kwargs):
            menu()
            try:
                choice: int = int(input())
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")
                return
            else:
                return func(choice, *args, **kwargs)
        return wrapper
    return decorator_func
