require_relative File.expand_path('crud', File.dirname(__FILE__))
require_relative File.expand_path('nemprestimo', File.dirname(__FILE__))
require_relative File.expand_path('nbibliotecario', File.dirname(__FILE__))
require_relative File.expand_path('nexemplar', File.dirname(__FILE__))
require_relative File.expand_path('nlivro', File.dirname(__FILE__))
require_relative File.expand_path('nusuario', File.dirname(__FILE__))



# Adiciona um empréstimo
emprestimo = Emprestimo.new('Livro B', 'Usuário 2', '2025-02-03', '2025-02-12', nil, 2)
emprestimo.salvar

# Testar salvar novo bibliotecário
bibliotecario = Bibliotecario.new('Maria Silva', 1)
bibliotecario.salvar

# Testar salvar novo exemplar
exemplar = Exemplar.new('Descrição Exemplar 1', 'Disponível', '2025-02-15')
exemplar.salvar

# Testar salvar novo livro
livro = Livro.new(1, 'Livro C', 'Autor C', 'Ficção', 300, 2020, 'Disponível', 10, 5)
livro.salvar

# Testar salvar novo usuário
usuario = Usuario.new('João Santos', '12345', 'Rua A, 123', '9999-9999', 'joao@example.com', ['Empréstimo 1', 'Empréstimo 2'])
usuario.salvar

# Carrega e imprime todos os empréstimos
emprestimos = Emprestimo.new('', '', '', '', '', '').abrir
emprestimos.each do |emp|
  puts "Livro: #{emp['livro']}, Usuário: #{emp['usuario']}, Data Empréstimo: #{emp['data_emprestimo']}, Data Devolução: #{emp['data_devolucao']}, Data Devolução Real: #{emp['data_devolucao_real']}, ID: #{emp['id']}"
end

# Carrega e imprime todos os bibliotecários
bibliotecarios = Bibliotecario.new('', '').abrir
bibliotecarios.each do |bibliotecario|
  puts "Nome: #{bibliotecario['nome']}, ID: #{bibliotecario['id']}"
end

# Carrega e imprime todos os exemplares
exemplares = Exemplar.new('', '', '').abrir
exemplares.each do |exemplar|
  puts "Descrição: #{exemplar['descricao']}, Situação: #{exemplar['situacao']}, Data Devolução: #{exemplar['data_devolucao']}"
end

# Carrega e imprime todos os livros
livros = Livro.new('', '', '', '', '', '', '', '', '').abrir
livros.each do |livro|
  puts "ID: #{livro['id']}, Título: #{livro['titulo']}, Autor: #{livro['autor']}, Gênero: #{livro['genero']}, Num. Páginas: #{livro['num_paginas']}, Ano Publicação: #{livro['ano_publicacao']}, Disponibilidade: #{livro['disponibilidade']}, Qtd Total: #{livro['qtd_total']}, Qtd Disponível: #{livro['qtd_disponivel']}"
end

# Carrega e imprime todos