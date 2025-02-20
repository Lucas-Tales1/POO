# usuario.rb
require 'json'
require_relative 'crud'

class Usuario < Crud
  attr_accessor :id_usuario, :nome, :numero_matricula, :endereco, :tel, :email, :senha, :historico_emprestimos

  def initialize(nome, numero_matricula, endereco, tel, email, senha, historico_emprestimos = [])
    super('dados/usuarios.json')
    @id_usuario = gerar_id
    @nome = nome
    @numero_matricula = numero_matricula
    @endereco = endereco
    @tel = tel
    @email = email
    @senha = senha
    @historico_emprestimos = historico_emprestimos
  end

  # Método para gerar um ID único para o usuário
  def gerar_id
    dados = listar
    # O ID será o próximo número disponível, ou 1 se não houver usuários
    dados.empty? ? 1 : dados.max_by { |usuario| usuario[:id_usuario] }[:id_usuario] + 1
  end

  # Método para listar usuários (usando o método da classe Crud)
  def abrir
    listar.each_with_index do |usuario, index|
      puts "#{index + 1}. ID: #{usuario[:id_usuario]}, Nome: #{usuario[:nome]}, Matrícula: #{usuario[:numero_matricula]}, Email: #{usuario[:email]}"
    end
  end

  # Método para salvar o usuário no arquivo
  def salvar
    dados = listar
    dados << { id_usuario: @id_usuario, nome: @nome, numero_matricula: @numero_matricula, endereco: @endereco, tel: @tel, email: @email, senha: @senha, historico_emprestimos: @historico_emprestimos }
    super(dados)  # Chama o método salvar da classe Crud para persistir os dados
  end

  # Método para adicionar um novo empréstimo ao histórico
  def adicionar_emprestimo(livro, data_emprestimo)
    emprestimo = { livro: livro, data_emprestimo: data_emprestimo }
    @historico_emprestimos << emprestimo
    salvar  # Regrava os dados após a atualização
  end
end
