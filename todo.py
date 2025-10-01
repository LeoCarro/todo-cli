import argparse
from typing import List
from core import create_task, list_tasks, mark_done, delete_task, clear_tasks, Task
import storage

def print_table(tasks: List[Task]) -> None:
    if not tasks:
        print("Nenhuma tarefa ainda. Use: python todo.py add "sua tarefa"")
        return
    # widths
    id_w = max(2, max(len(str(t.id)) for t in tasks))
    title_w = max(5, max(len(t.title) for t in tasks))
    status_w = len("status")
    print(f"{'id':>{id_w}}  {'titulo':<{title_w}}  {'status':<{status_w}}")
    print("-" * (id_w + title_w + status_w + 4))
    for t in tasks:
        status = "feito" if t.done else "pend."
        print(f"{t.id:>{id_w}}  {t.title:<{title_w}}  {status:<{status_w}}")


def main():
    parser = argparse.ArgumentParser(description="Gerenciador simples de TODOs (JSON)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Adicionar uma nova tarefa")
    p_add.add_argument("title", type=str, help="O texto da tarefa")

    p_list = sub.add_parser("list", help="Listar tarefas")

    p_done = sub.add_parser("done", help="Marcar tarefa como concluída")
    p_done.add_argument("id", type=int, help="ID da tarefa")

    p_del = sub.add_parser("delete", help="Excluir uma tarefa pelo ID")
    p_del.add_argument("id", type=int, help="ID da tarefa")

    p_clear = sub.add_parser("clear", help="Apagar TODAS as tarefas")

    args = parser.parse_args()
    tasks = storage.load_tasks()

    if args.command == "add":
        tasks = create_task(tasks, args.title)
        storage.save_tasks(tasks)
        print("✅ Tarefa adicionada.")
    elif args.command == "list":
        print_table(tasks)
    elif args.command == "done":
        try:
            tasks = mark_done(tasks, args.id)
            storage.save_tasks(tasks)
            print("✅ Tarefa marcada como concluída.")
        except ValueError as e:
            print(f"⚠️ {e}")
    elif args.command == "delete":
        try:
            tasks = delete_task(tasks, args.id)
            storage.save_tasks(tasks)
            print("🗑️ Tarefa excluída.")
        except ValueError as e:
            print(f"⚠️ {e}")
    elif args.command == "clear":
        tasks = clear_tasks()
        storage.save_tasks(tasks)
        print("🧹 Todas as tarefas foram removidas.")

if __name__ == "__main__":
    main()