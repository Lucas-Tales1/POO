require 'json'
require_relative 'CRUD'

class Bibliotecario < CRUD
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
end
