import argparse
from typing import List
from core import create_task, list_tasks, mark_done, delete_task, clear_tasks, Task
import storage

EPILOG = """
Exemplos de uso:
  python todo.py add "Comprar frutas"
  python todo.py list
  python todo.py done 1
  python todo.py delete 1
  python todo.py clear
"""

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gerenciador simples de TODOs (salva em todos.json na pasta do projeto).",
        epilog=EPILOG,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Adicionar uma nova tarefa")
    p_add.add_argument("title", type=str, help="O texto da tarefa (use aspas se houver espaços)")

    sub.add_parser("list", help="Listar todas as tarefas")

    p_done = sub.add_parser("done", help="Marcar tarefa como concluída (informe o ID)")
    p_done.add_argument("id", type=int, help="ID da tarefa (veja com 'python todo.py list')")

    p_del = sub.add_parser("delete", help="Excluir uma tarefa pelo ID")
    p_del.add_argument("id", type=int, help="ID da tarefa a excluir")

    sub.add_parser("clear", help="Apagar TODAS as tarefas (use com cuidado)")
    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    tasks = storage.load_tasks()

    if args.command == "add":
        tasks = create_task(tasks, args.title)
        storage.save_tasks(tasks)
        print("✅ Tarefa adicionada.")
    elif args.command == "list":
        # implementação da impressão entra no próximo passo
        print("lista (temporário)")
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
