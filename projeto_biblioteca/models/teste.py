from datetime import date
from emprestimo import Emprestimo
from bibliotecario import Bibliotecario
from exemplar import Exemplar
from livro import Livro
from usuario import Usuario

# Adiciona um empréstimo
Emprestimo.salvar_novo_emprestimo('Livro A', 'Usuário 1', '2025-02-01', '2025-02-10', '2025-02-09', 1)
# Testar salvar novo bibliotecário
Bibliotecario.salvar_novo_bibliotecario('Maria Silva', 1)

# Testar salvar novo exemplar
Exemplar.salvar_novo_exemplar('Descrição Exemplar 1', True, '2025-02-15')

# Testar salvar novo livro
Livro.salvar_novo_livro(1, 'Livro C', 'Autor C', 'Ficção', 300, 2020, 'Disponível', 10, 5)

# Testar salvar novo usuário
Usuario.salvar_novo_usuario('João Santos', '12345', 'Rua A, 123', '9999-9999', 'joao@example.com', ['Empréstimo 1', 'Empréstimo 2'])


# Carrega todos os empréstimos e imprime
emprestimos = Emprestimo.carregar_emprestimos()
for emprestimo in emprestimos:
    print(emprestimo)

# Carrega todos os bibliotecários e imprime
bibliotecarios = Bibliotecario.carregar_bibliotecarios()
for bibliotecario in bibliotecarios:
    print(bibliotecario)

# Carrega todos os exemplares e imprime
exemplares = Exemplar.carregar_exemplares()
for exemplar in exemplares:
    print(exemplar)

# Carrega todos os livros e imprime
livros = Livro.carregar_livros()
for livro in livros:
    print(livro)

# Carrega todos os usuários e imprime
usuarios = Usuario.carregar_usuarios()
for usuario in usuarios:
    print(usuario)

