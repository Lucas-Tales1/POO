require 'json'
require_relative 'crud'

class Bibliotecario < Crud
  attr_accessor :nome, :id

  def initialize(nome, id)
    super('dados/bibliotecarios.json')
    @nome = nome
    @id = id
  end

  def abrir
    listar
  end

  def salvar
    dados = listar
    dados << { nome: @nome, id: @id }
    super(dados)
  end
end
