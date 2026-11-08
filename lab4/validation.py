"""Проверка пользовательского ввода: тип числа, границы диапазона, повтор до корректного значения."""

from __future__ import annotations

from constants import M_MIN, M_MAX
from logger import log_error


def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """Проверить, что value лежит в [low, high]. Возвращает (True, "") или (False, сообщение)."""
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low:g})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high:g})."
    else:
        return True, ""


def input_number(prompt: str, low: float, high: float) -> float:
    """Запрашивать число, пока оно не окажется корректным и в пределах [low, high]."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw)
        except ValueError:
            msg = f"Ошибка: введено не число ('{raw}')."
            print(msg + " Повторите ввод.")
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_mass() -> float:
    """Ввод общей массы смеси M, кг (допустимо 1..10000)."""
    return input_number(f"Введите общую массу смеси M, кг ({M_MIN:g}..{M_MAX:g}): ",M_MIN, M_MAX)
