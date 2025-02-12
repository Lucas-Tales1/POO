require 'json'
require_relative 'CRUD'

class Exemplar < CRUD
  attr_accessor :descricao, :situacao, :data_devolucao

  def initialize(descricao, situacao, data_devolucao)
    super('exemplares.json')
    @descricao = descricao
    @situacao = situacao
    @data_devolucao = data_devolucao
  end

  def abrir
    listar
  end

  def salvar
    dados = listar
    dados << { descricao: @descricao, situacao: @situacao, data_devolucao: @data_devolucao }
    File.write(@caminho_arquivo, JSON.pretty_generate(dados))
  end
end
