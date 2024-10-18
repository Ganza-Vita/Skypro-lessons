import functools
import logging
import sys
from typing import Any, Callable, Optional

def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который логирует выполнение функции."""

    # Настройка логирования
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(message)s')
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                            format='%(asctime)s - %(message)s')

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logging.info(f"Запуск функции '{func.__name__}' с аргументами: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"Функция '{func.__name__}' завершена успешно, результат: {result}")
                return result
            except Exception as e:
                logging.error(f"Функция '{func.__name__}' вызвала ошибку: {type(e).__name__}. Входные параметры: {args}, {kwargs}")
                raise

        return wrapper
    return decorator