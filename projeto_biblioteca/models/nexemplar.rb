require 'json'
require_relative 'crud'

class Exemplar < Crud
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

  def listar
    if File.exist?(@caminho_arquivo)
      arquivo = File.read(@caminho_arquivo)
      JSON.parse(arquivo)
    else
      []
    end
  end
end
