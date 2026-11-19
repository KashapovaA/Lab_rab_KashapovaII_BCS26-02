from typing import List, Sequence

def check_window(window: int, n: int) -> None:
    try:
        is_positive_int = (window >= 1) and (int(window) == window)
    except (TypeError, ValueError) as err:
        raise ValueError(
            f"window должно быть целым числом >= 1 "
            f"(получено: {window!r}; причина: {err})"
        ) from err
    if not is_positive_int:
        raise ValueError(f"window должно быть целым числом >= 1 (получено: {window!r})")
    if window > n:
        raise ValueError(
            f"window не должен превышать длину ряда "
            f"(получено: window={window}, n={n})"
        )

def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """SMA"""
    n = len(data)
    check_window(window, n)
    running = sum(data[:window])
    result = [running / window]
    for i in range(window, n):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result

def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированное MA: окно нечётное, выход выровнен по центру.
    Точка i — среднее по окну, центр которого совпадает с i.
    Длина результата: len(data) - window + 1."""
    n = len(data)
    check_window(window, n)
    if window % 2 == 0:
        raise ValueError(
            f"для центрированного MA окно должно быть нечётным (получено: {window})"
        )
    half = window // 2
    return [
        sum(data[i - half:i + half + 1]) / window
        for i in range(half, n - half)
    ]

def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """EMA: экспоненциальное сглаживание.
    EMA[0] = data[0]
    EMA[i] = alpha * data[i] + (1 - alpha) * EMA[i - 1],  0 < alpha <= 1"""
    if not data:
        raise ValueError("Ряд пуст: расчёт EMA невозможен")
    try:
        is_valid = (0 < alpha) and (alpha <= 1) and (float(alpha) == alpha)
    except (TypeError, ValueError) as err:
        raise ValueError(
            f"alpha должно быть числом в интервале (0; 1] (получено: {alpha!r})"
        ) from err
    if not is_valid:
        raise ValueError(f"alpha должно быть числом в интервале (0; 1] (получено: {alpha!r})")
    result = [float(data[0])]
    for i in range(1, len(data)):
        result.append(alpha * data[i] + (1 - alpha) * result[-1])
    return result