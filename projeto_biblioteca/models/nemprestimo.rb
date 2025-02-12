require 'json'
require_relative 'crud'

class Emprestimo < Crud
  attr_accessor :livro, :usuario, :data_emprestimo, :data_devolucao, :data_devolucao_real, :id

  def initialize(livro, usuario, data_emprestimo, data_devolucao, data_devolucao_real, id)
    super('dados/emprestimos.json')
    @livro = livro
    @usuario = usuario
    @data_emprestimo = data_emprestimo
    @data_devolucao = data_devolucao
    @data_devolucao_real = data_devolucao_real
    @id = id
  end

  def abrir
    listar
  end

  def salvar
    dados = listar
    dados << { livro: @livro, usuario: @usuario, data_emprestimo: @data_emprestimo, data_devolucao: @data_devolucao, data_devolucao_real: @data_devolucao_real, id: @id }
    super(dados)
  end
end
