"""Меню выбора типа смеси через match-case."""

from __future__ import annotations

from constants import BETON, CERAMIC, SPLAV

def show_menu() -> None:
    """Вывести меню смесей."""
    print("\nВыберите тип смеси:")
    print("  1 - бетон")
    print("  2 - керамика")
    print("  3 - сплав")
    print("  0 - выход")

def select_smes() -> tuple[str, dict[str, float]] | None:
    """Запрашивать пункт меню, пока он не будет корректным.
    Возвращает (название смеси, состав) или None при выборе выхода."""
    while True:
        choice = input("Введите номер пункта (0..3): ").strip()
        match choice:
            case "1":
                return "бетон", BETON
            case "2":
                return "керамика", CERAMIC
            case "3":
                return "сплав", SPLAV
            case "0":
                return None
            case _:
                print("Ошибка: такого пункта нет. Повторите ввод.")
