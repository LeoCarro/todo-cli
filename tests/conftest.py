# tests/conftest.py
# Garante que a raiz do projeto (onde ficam core.py, storage.py, todo.py)
# esteja no sys.path durante os testes.
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # .../todo-cli
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))