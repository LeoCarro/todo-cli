# TODO CLI (projeto iniciante em Python)

Um aplicativo **de linha de comando** para gerenciar tarefas usando **apenas Python puro** e arquivo `todos.json` como armazenamento.

## ✨ O que você vai aprender
- Estruturar um projeto Python simples
- Ler e escrever arquivos JSON
- Criar **subcomandos** com `argparse` (ex.: `add`, `list`, `done`, `delete`, `clear`)
- Escrever **testes** com `pytest`
- Colaborar via **GitHub Flow** (branches, pull requests, code review)

## 📦 Instalação (local)
1) Recomendo Python 3.10+ instalado.
2) Crie e ative um ambiente virtual:
```bash
python -m venv .venv
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
```
3) Instale as dependências de desenvolvimento (apenas pytest):
```bash
pip install -r requirements.txt
```

## ▶️ Uso
Todos os comandos são executados a partir da raiz do projeto.

Adicionar uma tarefa:
```bash
python todo.py add "Comprar frutas"
```

Listar tarefas:
```bash
python todo.py list
```

Marcar como concluída (use o ID mostrado na listagem):
```bash
python todo.py done 1
```

Excluir uma tarefa:
```bash
python todo.py delete 1
```

Apagar **todas** as tarefas:
```bash
python todo.py clear
```

> As tarefas ficam salvas em `todos.json` no diretório do projeto.

## 🧪 Testes
```bash
pytest -q
```

## 👥 Colaboração (GitHub Flow)
1. **Um de vocês** cria o repositório no GitHub e adiciona o outro como **Collaborator** (Settings → Collaborators).
2. Cada pessoa **clona** o repo:
```bash
git clone <URL_DO_REPO>
cd todo-cli
```
3. **Crie uma branch por funcionalidade**:
```bash
git checkout -b feature/add-command
```
4. Faça commits pequenos e descritivos:
```bash
git add .
git commit -m "feat: add command to create tasks"
git push -u origin feature/add-command
```
5. **Abra um Pull Request (PR)** no GitHub, peça revisão do colega.
6. Após aprovado, **merge** na `main` e **cada um puxa as novidades**:
```bash
git checkout main
git pull origin main
```
7. Para evitar conflitos, **sempre** atualize sua branch com a `main` antes de continuar:
```bash
git checkout feature/sua-branch
git pull --rebase origin main
```

## 🗂️ Estrutura
```
todo-cli/
├── todo.py            # Interface de linha de comando (CLI)
├── core.py            # Lógica pura de tarefas (testável)
├── storage.py         # Leitura/escrita do arquivo JSON
├── tests/
│   └── test_core.py   # Testes unitários do core
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Próximos passos (sugestões)
- Campo `due_date` (prazo) e filtro por atrasadas
- Prioridade (baixa/média/alta)
- Exportar para CSV
- Persistir em `~/.todo_cli/todos.json` por usuário