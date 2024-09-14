import logging

import pytest

from utils.decorators import log


# Пример функции для тестирования
@log()
def successful_function(a, b):
    return a + b


# Функция с возможной ошибкой
@log()
def function_with_exception(a, b):
    return a / b


def test_successful_function(capsys):
    result = successful_function(3, 4)

    # Проверяем результат функции
    assert result == 7

    # Получаем вывод из консоли
    captured = capsys.readouterr()

    # Проверяем логи
    assert "Starting successful_function with args: (3, 4) kwargs: {}" in captured.out
    assert "successful_function ok: Result: 7" in captured.out


def test_function_with_exception(capsys):
    with pytest.raises(ZeroDivisionError):
        function_with_exception(10, 0)

    # Получаем вывод из консоли
    captured = capsys.readouterr()

    # Проверяем логи
    assert "Starting function_with_exception with args: (10, 0) kwargs: {}" in captured.out
    assert "function_with_exception error: ZeroDivisionError. Inputs: (10, 0), {}" in captured.out
