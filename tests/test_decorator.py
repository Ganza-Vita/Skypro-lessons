import pytest
import logging
from src.decorators import log  # Замените 'your_module' на имя вашего модуля, где находится декоратор

# Функция для тестирования
@log()
def sample_function(x: int, y: int) -> int:
    return x + y

@log()
def function_with_error(x: int):
    return x / 0  # Создаем ошибку деления на ноль для теста

# Тесты
def test_sample_function(caplog):
    with caplog.at_level(logging.INFO):
        result = sample_function(3, 5)
    assert result == 8
    assert "Запуск функции 'sample_function' с аргументами: (3, 5), {}" in caplog.text
    assert "Функция 'sample_function' завершена успешно, результат: 8" in caplog.text

def test_function_with_error(caplog):
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ZeroDivisionError):
            function_with_error(5)
    assert "Функция 'function_with_error' вызвала ошибку: ZeroDivisionError. Входные параметры: (5,), {}" in caplog.text