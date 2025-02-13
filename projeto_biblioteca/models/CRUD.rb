require 'json'
require 'fileutils'

class Crud
  attr_accessor :caminho_arquivo

  def initialize(caminho_arquivo)
    @caminho_arquivo = caminho_arquivo
  end

  def salvar(dados)
    FileUtils.mkdir_p(File.dirname(@caminho_arquivo))
    File.write(@caminho_arquivo, JSON.pretty_generate(dados))
  end

  # Novo método para inserir um item
  def inserir(novo_item)
    dados = listar
    dados << novo_item
    salvar(dados)
  end

  def listar
    if File.exist?(@caminho_arquivo)
      arquivo = File.read(@caminho_arquivo)
      JSON.parse(arquivo, symbolize_names: true) # Usa symbolize_names: true para trabalhar com símbolos
    else
      []
    end
  end

  # Novo método para atualizar um item existente
  def atualizar(id, novos_dados)
    dados = listar
    item = dados.find { |d| d[:id] == id }
    if item
      item.merge!(novos_dados)
      salvar(dados)
    else
      puts "Item com ID #{id} não encontrado."
    end
  end

  # Novo método para excluir um item
  def excluir(id)
    dados = listar
    dados_reduzidos = dados.reject { |d| d[:id] == id }
    if dados_reduzidos.size < dados.size
      salvar(dados_reduzidos)
      puts "Item com ID #{id} excluído com sucesso."
    else
      puts "Item com ID #{id} não encontrado."
    end
  end
end
