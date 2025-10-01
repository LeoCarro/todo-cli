from dataclasses import dataclass, asdict
from typing import List, Optional
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created_at: str = ""
    finished_at: Optional[str] = None

def now_iso() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

def next_id(tasks: List[Task]) -> int:
    return (max((t.id for t in tasks), default=0) + 1)

def create_task(tasks: List[Task], title: str) -> List[Task]:
    new = Task(id=next_id(tasks), title=title.strip(), done=False, created_at=now_iso())
    return tasks + [new]

def list_tasks(tasks: List[Task]) -> List[Task]:
    return tasks

def mark_done(tasks: List[Task], task_id: int) -> List[Task]:
    updated: List[Task] = []
    found = False
    for t in tasks:
        if t.id == task_id:
            found = True
            if not t.done:
                t = Task(id=t.id, title=t.title, done=True, created_at=t.created_at, finished_at=now_iso())
        updated.append(t)
    if not found:
        raise ValueError(f"Tarefa com id {task_id} não encontrada.")
    return updated

def delete_task(tasks: List[Task], task_id: int) -> List[Task]:
    new = [t for t in tasks if t.id != task_id]
    if len(new) == len(tasks):
        raise ValueError(f"Tarefa com id {task_id} não encontrada.")
    return new

def clear_tasks() -> List[Task]:
    return []

def to_dicts(tasks: List[Task]) -> List[dict]:
    return [asdict(t) for t in tasks]

def from_dicts(data: List[dict]) -> List[Task]:
    result: List[Task] = []
    for d in data:
        result.append(Task(**d))
    return result