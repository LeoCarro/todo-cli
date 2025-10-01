import pytest
from core import create_task, list_tasks, mark_done, delete_task, clear_tasks

def test_flow():
    tasks = []
    tasks = create_task(tasks, "Estudar Python")
    tasks = create_task(tasks, "Comprar frutas")
    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[1].id == 2

    listed = list_tasks(tasks)
    assert len(listed) == 2

    tasks = mark_done(tasks, 1)
    assert tasks[0].done is True

    tasks = delete_task(tasks, 2)
    assert len(tasks) == 1
    assert tasks[0].id == 1

    tasks = clear_tasks()
    assert tasks == []

def test_mark_done_inexistente():
    with pytest.raises(ValueError):
        mark_done([], 99)