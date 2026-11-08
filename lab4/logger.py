"""Журнал ошибок ввода: хранит записи в памяти и дописывает их в файл."""

from __future__ import annotations

import datetime

from constants import LOG_FILE

_entries: list[str] = []

def log_error(message: str) -> None:
    """Записать сообщение об ошибке ввода с отметкой времени."""
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{stamp}] {message}"
    _entries.append(entry)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except OSError:
        pass

def get_entries() -> list[str]:
    """Вернуть копию журнала ошибок."""
    return list(_entries)

def clear() -> None:
    """Очистить журнал в памяти."""
    _entries.clear()
