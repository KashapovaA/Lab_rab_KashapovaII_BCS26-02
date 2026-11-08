"""Лабораторная работа 2, вариант 6"""

from menu import show_menu, select_smes
from validation import input_mass
from operations import component_masses, fractions_sum, fractions_sum_ok, part_class

def print_result(name: str, fractions: dict[str, float], total_mass: float) -> None:
    """Вывести результаты расчёта с единицами измерения."""
    print("\nРезультаты")
    print(f"Тип смеси: {name}")
    print("Массы компонентов:")
    for comp, mass in component_masses(total_mass, fractions).items():
        print(f"  {comp:<12} -> {mass:.2f} кг")

    total = fractions_sum(fractions)
    if fractions_sum_ok(fractions):
        print(f"Сумма долей: {total:.2f} - состав корректный")
    else:
        print(f"Сумма долей: {total:.4f} - ошибка состава, сумма не равна 1")

    print(f"Класс партии: {part_class(total_mass)}")

def main() -> None:
    """Главный цикл программы."""
    print("=== Расчёт компонентов технологической смеси ===")
    while True:
        show_menu()
        selected = select_smes()
        if selected is None:
            print("Работа завершена.")
            break
        name, fractions = selected
        total_mass = input_mass()
        print_result(name, fractions, total_mass)

if __name__ == "__main__":
    main()
