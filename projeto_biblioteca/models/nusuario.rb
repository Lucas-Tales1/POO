require 'json'
require_relative 'crud'

class Usuario < Crud
  attr_accessor :nome, :numero_matricula, :endereco, :tel, :email, :senha, :historico_emprestimos

  def initialize(nome, numero_matricula, endereco, tel, email, senha, historico_emprestimos)
    super('dados/usuarios.json')
    @nome = nome
    @numero_matricula = numero_matricula
    @endereco = endereco
    @tel = tel
    @email = email
    @senha = senha
    @historico_emprestimos = historico_emprestimos
  end

  def abrir
    listar
  end

  def salvar
    dados = listar
    dados << { nome: @nome, numero_matricula: @numero_matricula, endereco: @endereco, tel: @tel, email: @email, senha: @senha, historico_emprestimos: @historico_emprestimos }
    super(dados)
  end
end
