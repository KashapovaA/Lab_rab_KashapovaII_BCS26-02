# Лабораторная работа 5 — вариант 6

Модульное консольное приложение «Алгоритмическая обработка числовых рядов».
Вариант 6: ряд «цена акции» (случайное блуждание), максимальная просадка,
SMA и EMA в одном CSV, краевой случай k > n.

## Структура

```
num_series_app/
├── num_series/
│   ├── __init__.py          # экспорт публичного API пакета
│   ├── generator.py         # random / sine / trend / stock (вариант 6)
│   ├── stats.py             # среднее, медиана, размах + max_drawdown
│   ├── moving_average.py    # SMA (бегущая сумма), CMA, EMA, бенчмарк
│   ├── deque_average.py     # SMA/CMA/EMA через collections.deque (5.1)
│   ├── io_json.py           # сохранение и чтение JSON
│   └── io_file.py           # чтение txt/csv, auto-парсер
├── main.py                  # CLI: связывает всё вместе
└── README.md
```

## Запуск

```bash
# Вариант 6 по умолчанию: n=1000, k=10, ряд «цена акции»
python main.py --seed 42

# Классический короткий запуск
python main.py --kind sine --n 20 --window 3 --seed 7

# Просадка + SMA/EMA в один CSV
python main.py --n 800 --window 10 --compare-csv out.csv

# Краевой случай: окно больше ряда
python main.py --n 50 --window 100

# Бенчмарк list vs deque
python main.py --n 1000 --window 10 --benchmark

# Сохранение / чтение
python main.py --n 800 --save data/stock.json
python main.py --load data/stock.json --window 10
```

## Вариант 6

- Ряд: `p[0] = 100`, `p[i] = p[i-1] * (1 + uniform(-0.02, 0.02))` — 800 чисел
  (длина задаётся через `--n`, по варианту 800; по умолчанию CLI — 1000).
- Доп. показатель: максимальная просадка (max drawdown) — разница между
  локальным максимумом и последующим минимумом; считается за один проход
  O(n), выводятся величина, пик и минимум с индексами.
- Скользящие средние: SMA и EMA (alpha по умолчанию `2/(k+1)`) выводятся
  в одном CSV (`--compare-csv out.csv`): колонки `i, value, sma_k, ema`.
- Краевой случай: при `k > n` SMA возвращает пустой список, CLI печатает
  предупреждение и завершается с кодом 0.

## Реализация SMA

Через бегущую сумму — O(n) вместо наивных O(n·k):

```
running = sum(data[:window])
result = [running / window]
for i in range(window, len(data)):
    running += data[i] - data[i - window]
    result.append(running / window)
```

## Замер производительности (5.1)

```bash
python main.py --kind stock --n 5000 --window 20 --benchmark
```