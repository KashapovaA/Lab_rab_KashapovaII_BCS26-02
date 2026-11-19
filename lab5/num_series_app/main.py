"""Точка входа: демонстрация модульного приложения обработки числовых рядов.
Запуск:
python main.py --kind sine --n 20 --window 3 --alpha 0.3 --seed 7
Параметры:
--kind тип ряда: random | sine | trend (по умолчанию: sine)
--n количество точек в ряде (по умолчанию: 20)
--window размер окна для скользящей средней (по умолчанию: 3)
--alpha коэффициент сглаживания для EMA (по умолчанию: 0.3)
--seed зерно ГПСЧ для воспроизводимости (по умолчанию: 42)
"""
from __future__ import annotations
import argparse
import csv
import sys
from typing import List, Optional, Tuple

from num_series import (
    random_series, sine_series, trend_series, summarize,
    simple_moving_average, centered_moving_average, exponential_moving_average
)
# ---------------------------------------------------------------------------
# Фабрика ряда
# ---------------------------------------------------------------------------

def build_series(kind: str, n: int, seed: int) -> List[float]:
    """Генерирует ряд заданного типа."""
    if kind == "random":
        return random_series(n, low=-50, high=50, seed=seed)
    if kind == "sine":
        return sine_series(n, amplitude=10, frequency=2, noise=1.5, seed=seed)
    if kind == "trend":
        return trend_series(n, start=0, step=1.0, noise=0.5, seed=seed)
    raise ValueError(f"Неизвестный тип ряда: {kind!r}")

def obtain_series(args: argparse.Namespace) -> Tuple[List[float], str]:
    """Возвращает (ряд, описание источника)."""
    if args.load:
        data = load_series_auto(args.load)
        return data, f"файл: {args.load}"
    data = build_series(args.kind, args.n, args.seed)
    return data, f"сгенерирован ({args.kind}, n={args.n}, seed={args.seed})"

# ---------------------
# Печать
# ---------------------

def print_series(title: str, values: List[float], fmt: str = "{:>10.3f}") -> None:
    print(f"\n{title} (n={len(values)}):")
    print("  " + " ".join(fmt.format(v) for v in values))
def print_header(source: str) -> None:
    print("=" * 60)
    print(f"Источник данных: {source}")
    print("-" * 60)
def print_stats(stats: dict) -> None:
    print(f"Среднее арифметическое : {stats['mean']:>10.4f}")
    print(f"Медиана                : {stats['median']:>10.4f}")
    print(f"Размах (max - min)     : {stats['spread']:>10.4f}")
    print(f"min / max              : {stats['min']:>10.4f} / {stats['max']:.4f}")
def print_footer() -> None:
    print("=" * 60)

# ---------------------------------------------------------------------------
# Разбор аргументов
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Алгоритмическая обработка числовых рядов",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--kind",
        choices=["random", "sine", "trend"],
        default="sine",
        help="тип генерируемого ряда",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=20,
        help="количество точек в ряде",
    )
    parser.add_argument(
        "--window",
        type=int,
        default=3,
        help="размер окна для скользящей средней",
    )
    parser.add_argument(
        "--alpha",
        type=float,
        default=0.3,
        help="коэффициент сглаживания для EMA, 0 < alpha <= 1",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="зерно ГПСЧ для воспроизводимости",
    )
    parser.add_argument(
        "--load",
        metavar="FILE",
        help="загрузить ряд из файла (автоматически определяется формат)",
    )
    parser.add_argument(
        "--export",
        metavar="FILE",
        help="экспорт результатов в CSV (только исходный ряд)",
    )
    return parser

# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        data, source = obtain_series(args)
        stats = summarize(data)
        sma = simple_moving_average(data, args.window)
        ema = exponential_moving_average(data, args.alpha)
        cma = (
            centered_moving_average(data, args.window)
            if args.window % 2 == 1 else None
        )
    except ValueError as err:
        print(f"Ошибка: {err}", file=sys.stderr)
        return 1

    # Экспорт в CSV
    if args.export:
        with open(args.export, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["i", "value"])
            for i, v in enumerate(data):
                w.writerow([i, v])
        print(f"Экспортировано в {args.export}")
    print_header(source)
    print_stats(stats)
    print_series("Исходный ряд", data)
    print_series(f"SMA (window={args.window})", sma)
    print_series(f"EMA (alpha={args.alpha})", ema)
    if cma is not None:
        print_series(f"Центрированное MA (window={args.window})", cma)
    print_footer()
    return 0
if __name__ == "__main__":
    raise SystemExit(main())