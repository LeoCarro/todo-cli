import json
from pathlib import Path
from typing import List
from core import Task, to_dicts, from_dicts

DATA_FILE = Path(__file__).resolve().parent / "todos.json"

def load_tasks() -> List[Task]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return from_dicts(data)

def save_tasks(tasks: List[Task]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(to_dicts(tasks), f, ensure_ascii=False, indent=2)