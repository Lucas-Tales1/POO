require 'json'
require_relative 'crud'

class Usuario < Crud
  attr_accessor :nome, :numero_matricula, :endereco, :tel, :email, :historico_emprestimos

  def initialize(nome, numero_matricula, endereco, tel, email, historico_emprestimos)
    super('usuarios.json')
    @nome = nome
    @numero_matricula = numero_matricula
    @endereco = endereco
    @tel = tel
    @email = email
    @historico_emprestimos = historico_emprestimos
  end

  def abrir
    listar
  end

  def salvar
    dados = listar
    dados << { nome: @nome, numero_matricula: @numero_matricula, endereco: @endereco, tel: @tel, email: @email, historico_emprestimos: @historico_emprestimos }
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
