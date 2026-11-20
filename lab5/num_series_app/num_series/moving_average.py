from __future__ import annotations

import time
from collections import deque
from typing import Dict, List, Sequence

def check_window(window: int, n: int) -> None:
    """Валидация окна: целое >= 1 и не больше длины ряда."""
    if not isinstance(window, int) or isinstance(window, bool):
        raise ValueError(f"window должен быть целым, получено: {window!r}")
    if window < 1:
        raise ValueError(f"window должен быть >= 1, получено: {window}")
    if window > n:
        raise ValueError(
            f"window ({window}) больше длины ряда ({n}) — SMA невозможна"
        )

def _check_alpha(alpha: float) -> None:
    if not (0 < alpha <= 1):
        raise ValueError(f"alpha должен быть в (0, 1], получено: {alpha}")

def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """SMA в точке i — среднее по window последним точкам.

    running += data[i] - data[i - window]  — на каждом шаге сумма
    обновляется за O(1). Длина результата: len(data) - window + 1.

    Пример:
    >>> simple_moving_average([1, 2, 3, 4, 5], 3)
    [2.0, 3.0, 4.0]
    """
    if not data:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    check_window(window, len(data))

    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result

def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированное МА: окно нечётное, результат выровнен по центру.

    Для чётного window выбрасывается ValueError.
    """
    if not data:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError(
            f"Центрированное МА требует нечётного window, получено: {window}"
        )
    half = window // 2
    n = len(data)
    return [
        sum(data[i - half:i + half + 1]) / window
        for i in range(half, n - half)
    ]

def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """EMA[0] = data[0]; EMA[i] = alpha*data[i] + (1-alpha)*EMA[i-1]."""
    if not data:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    _check_alpha(alpha)
    result = [float(data[0])]
    prev = result[0]
    for x in data[1:]:
        prev = alpha * x + (1.0 - alpha) * prev
        result.append(prev)
    return result

def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]:
    """SMA с использованием deque (двусторонней очереди)."""
    if not data:
        raise ValueError("Ряд пуст: расчёт скользящей средней невозможен")
    check_window(window, len(data))
    result: List[float] = []
    d = deque()
    running_sum = 0.0
    for x in data:
        d.append(x)
        running_sum += x
        if len(d) > window:
            running_sum -= d.popleft()
        if len(d) == window:
            result.append(running_sum / window)
    return result

def benchmark_moving_average(data: Sequence[float],
                             window: int,
                             repeats: int = 1000) -> Dict[str, float]:
    """Замеряет среднее время SMA для реализаций на list и deque.
возвращает словарь с ключами 'list' и 'deque' (время в секундах).
 """
 # Проверка корректности окна (выбросит ValueError при необходимости)
    check_window(window, len(data))
 # Замер для list-реализации (существующая simple_moving_average) 
    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average(data, window)
    t_list = (time.perf_counter() - t0) / repeats
# Замер для deque-реализации
    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average_deque(data, window)
    t_deque = (time.perf_counter() - t0) / repeats

    return {"list": t_list, "deque": t_deque}