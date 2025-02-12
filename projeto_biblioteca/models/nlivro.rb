require 'json'
require_relative 'CRUD'

class Livro < CRUD
  attr_accessor :id, :titulo, :autor, :genero, :num_paginas, :ano_publicacao, :disponibilidade, :qtd_total, :qtd_disponivel

  def initialize(id, titulo, autor, genero, num_paginas, ano_publicacao, disponibilidade, qtd_total, qtd_disponivel)
    super('livros.json')
    @id = id
    @titulo = titulo
    @autor = autor
    @genero = genero
    @num_paginas = num_paginas
    @ano_publicacao = ano_publicacao
    @disponibilidade = disponibilidade
    @qtd_total = qtd_total
    @qtd_disponivel = qtd_disponivel
  end

  def abrir
    listar
  end

  def salvar
    dados = listar
    dados << { id: @id, titulo: @titulo, autor: @autor, genero: @genero, num_paginas: @num_paginas, ano_publicacao: @ano_publicacao, disponibilidade: @disponibilidade, qtd_total: @qtd_total, qtd_disponivel: @qtd_disponivel }
    File.write(@caminho_arquivo, JSON.pretty_generate(dados))
  end
end
