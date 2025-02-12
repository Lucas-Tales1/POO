require 'json'
require 'fileutils'

class Crud
  attr_accessor :caminho_arquivo

  def initialize(caminho_arquivo)
    @caminho_arquivo = caminho_arquivo
  end

  def listar
    if File.exist?(@caminho_arquivo)
      arquivo = File.read(@caminho_arquivo)
      JSON.parse(arquivo)
    else
      []
    end
  end

  def salvar(dados)
    FileUtils.mkdir_p(File.dirname(@caminho_arquivo))
    File.write(@caminho_arquivo, JSON.pretty_generate(dados))
  end
end
