# Contribuição

## Padrão de Branches
- `feature/<resumo>` para novas funcionalidades (ex.: `feature/add-command`)
- `fix/<resumo>` para correções
- `docs/<resumo>` para mudanças só em documentação
- `tests/<resumo>` para testes

## Padrão de Commits (sugestão)
- `feat: ...` nova funcionalidade
- `fix: ...` correção
- `docs: ...` documentação
- `test: ...` testes
- `refactor: ...` refatoração (sem mudar comportamento)

## Pull Requests
1. Atualize sua branch com `main` (`git pull --rebase origin main`).
2. Rode `pytest -q` e garanta que tudo passa.
3. Abra o PR, descreva **o que** e **por que**.
4. Responda comentários de revisão; faça ajustes se necessário.