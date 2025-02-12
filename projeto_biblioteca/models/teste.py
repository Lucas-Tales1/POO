from datetime import date
from emprestimo import Emprestimo

# Adiciona um empréstimo
Emprestimo.salvar_novo_emprestimo('Livro A', 'Usuário 1', '2025-02-01', '2025-02-10', '2025-02-09', 1)

# Carrega todos os empréstimos e imprime
emprestimos = Emprestimo.carregar_emprestimos()
for emprestimo in emprestimos:
    print(emprestimo)
