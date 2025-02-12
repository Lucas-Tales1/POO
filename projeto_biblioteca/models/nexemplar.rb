require 'json'
require_relative 'crud'

class Exemplar < Crud
  attr_accessor :descricao, :situacao, :data_devolucao

  def initialize(descricao, situacao, data_devolucao)
    super('dados/exemplares.json')
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
    super(dados)
  end
end
