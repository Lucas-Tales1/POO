require 'json'
require_relative 'CRUD'

class Emprestimo < CRUD
  attr_accessor :livro, :usuario, :data_emprestimo, :data_devolucao, :data_devolucao_real, :id

  def initialize(livro, usuario, data_emprestimo, data_devolucao, data_devolucao_real, id)
    super('emprestimos.json')
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
    File.write(@caminho_arquivo, JSON.pretty_generate(dados))
  end
end
