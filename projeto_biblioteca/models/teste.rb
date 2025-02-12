require_relative 'crud'
require_relative 'nexemplar'

# Crie uma nova instância de Exemplar
exemplar1 = Exemplar.new('Descrição Exemplar 1', 'Disponível', '2025-02-15')
# Salve o exemplar
exemplar1.salvar

# Crie outra instância de Exemplar
exemplar2 = Exemplar.new('Descrição Exemplar 2', 'Emprestado', '2025-03-01')
# Salve o segundo exemplar
exemplar2.salvar

# Carrega todos os exemplares e imprime
exemplares = Exemplar.new('', '', '').abrir
exemplares.each do |exemplar|
  puts "Descrição: #{exemplar['descricao']}, Situação: #{exemplar['situacao']}, Data Devolução: #{exemplar['data_devolucao']}"
end
