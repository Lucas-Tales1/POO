require 'json'
require_relative 'crud'

class Bibliotecario < Crud
  attr_accessor :nome, :id

  def initialize(nome, id)
    super('bibliotecarios.json')
    @nome = nome
    @id = id
  end

  def abrir
    listar
  end

  def salvar
    dados = listar
    dados << { nome: @nome, id: @id }
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
