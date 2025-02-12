require_relative 'nemprestimo'

# Adiciona um empréstimo
emprestimo = Emprestimo.new('Livro B', 'Usuário 2', '2025-02-03', '2025-02-12', nil, 2)
emprestimo.salvar

# Exibe todos os empréstimos
emprestimos = emprestimo.abrir
emprestimos.each do |emp|
  puts "Livro: #{emp['livro']}, Usuário: #{emp['usuario']}, Data Empréstimo: #{emp['data_emprestimo']}, Data Devolução: #{emp['data_devolucao']}, Data Devolução Real: #{emp['data_devolucao_real']}, ID: #{emp['id']}"
end
