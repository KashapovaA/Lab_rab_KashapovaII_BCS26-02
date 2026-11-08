"""Расчёты: массы компонентов, класс партии, проверка суммы долей."""

from __future__ import annotations

import math

from constants import SMALL_LIMIT, LARGE_LIMIT, FRACTION_CHECK

def component_masses(total_mass: float, fractions: dict[str, float]) -> dict[str, float]:
    """Рассчитать массу каждого компонента: m_i = M * fraction_i, кг."""
    return {name: total_mass * share for name, share in fractions.items()}

def fractions_sum(fractions: dict[str, float]) -> float:
    """Сумма долей компонентов."""
    return sum(fractions.values())

def fractions_sum_ok(fractions: dict[str, float]) -> bool:
    """Проверить, что сумма долей равна 1 (с учётом погрешности дробных чисел)."""
    return math.isclose(fractions_sum(fractions), 1.0, abs_tol=FRACTION_CHECK)

def part_class(total_mass: float) -> str:
    """Класс партии по массе через if-elif-else.
M < 100 - малая партия; 100 <= M <= 1000 - средняя; M > 1000 - крупная."""
    if total_mass < SMALL_LIMIT:
        return "малая партия"
    elif total_mass <= LARGE_LIMIT:
        return "средняя партия"
    else:
        return "крупная партия"
