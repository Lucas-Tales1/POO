require 'json'

class CRUD
  def initialize(caminho_arquivo)
    @caminho_arquivo = caminho_arquivo
  end

  def inserir(item)
    dados = listar
    dados << item
    salvar(dados)
  end

  def listar
    if File.exist?(@caminho_arquivo)
      dados = File.read(@caminho_arquivo)
      JSON.parse(dados, symbolize_names: true)
    else
      []
    end
  rescue
    []
  end

  def atualizar(id, novo_item)
    dados = listar
    dados.map! { |item| item[:id] == id ? novo_item : item }
    salvar(dados)
  end

  def excluir(id)
    dados = listar
    dados.reject! { |item| item[:id] == id }
    salvar(dados)
  end

  def salvar(dados)
    File.write(@caminho_arquivo, JSON.pretty_generate(dados))
  end
end
