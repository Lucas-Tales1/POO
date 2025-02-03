# Projeto Biblioteca
## Sistema de biblioteca

### Histórico da Revisão 

|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 27/01/2025 |  **`1.00`** | Versão Inicial  | Lucas Tales |

### 1. Objetivo do Projeto 

O sistema tem como objetivo gerenciar eficientemente o acervo de livros de uma
biblioteca e seus usuários, apoiar a educação e a cultura ao facilitar o acesso ao
conhecimento e promover a leitura.

### 2. Descrição do Problema 

|         __        | __   |
|:------------------|:-----|
| **_O problema_**    | Gerir os empréstimos e devoluções de uma biblioteca de forma eficiente e precisa.  |
| **_afetando_**      | Bibliotecários e a biblioteca que disponibilizam o acesso aos livros. |
| **_cujo impacto é_**| Dificuldade no gerenciamento de empréstimos e perda de livros. |
| **_uma boa solução seria_** | Um sistema de biblioteca que permita aos bibliotecários gerir de maneira mais simples e com maior precisão os livros que foram emprestados e devolvidos. |

### 3. Descrição dos Usuários

| Nome | Descrição | Responsabilidades |
|:---  |:--- |:--- |
| Bibliotecário  | Realiza as atividades básicas para o início da operação do sistema | Mantém o cadastro dos livros e usuários e gere os empréstimos |
| Usuário  | Realiza os empréstimos e devoluções | Realiza o próprio cadastro |

### 4. Descrição do Ambiente dos Usuários

Com a grande quantidade de livros que uma biblioteca pode oferecer e a quantidade de leitores que querem fazer seus empréstimos torna-se difícil para o bibliotecário conseguir gerir com precisão isso.

Desta forma, a ideia central do sistema é permitir que o biliotecário registre os empréstimos que foram feitos por cada leitor, ou os próprios leitores fazerem esse registro. Com isso, o sistema pode garantir um melhor controle dos livros que foram emprestados e com quem estão.

### 5. Principais Necessidades dos Usuários

Para o Bibliotecário, conseguir gerir de forma precisa e simples os empréstimos e devoluções.

Para os clientes, buscar os livros que estão disponíveis com mais facilidade e registrar seus empréstimos por conta própria.

### 6.	Alternativas Concorrentes

As alternativas concorrentes são sistemas de biblioteca no geral. 

### 7.	Visão Geral do Produto

Em resumo, o sistema de biblioteca é uma aplicação que permite o bibliotecário gerir com maior precisão os livros que foram emprestados e permite o usuário achar o livro que deseja pegar emprestado com maior facilidade.

O sistema deve ter uma interface amigável e simples para tornar fácil sua utilização tanto pelo bibliotecário quanto pelo usuário.

### 8. Requisitos Funcionais

| Código | Nome | Descrição |
|:---  |:--- |:--- |
| RF01 | Entrar no sistema | Usuários devem logar no sistema para acessar as funcionalidades relacionadas ao empréstimo de livros |
| RF02 | Cadastro de usuários | Bibliotecário mantém o cadastro dos usuários que pedem os empréstimos |
| RF03 | Gerenciamento de empréstimos |  Bibliotecário vê quem pegou algum livro emprestado |
| RF04 | Gerenciamento da devoluções | Bibliotecário vê quem devolveu os livros e se foi dentro do prazo |
| RF05 | Cadastrar-se | usuário pode realizar o próprio cadastro |
| RF06 | Consultar livros disponíveis | usuário pode ver quais livros estão disponíveis para empréstimo |
| RF07 | Histórico de empréstimos | Usuário pode ver o histórico de empréstimos que ele fez |


### 9. Requisitos Não-funcionais

 Código | Nome | Descrição | Categoria | Classificação
|:---  |:--- |:--- |:--- |:--- |
| RNF01 | Design simples | O sistema deve ter uma interface simples | Usabilidade| Obrigatório |
| RNF02 | Controle de acesso | Só usuários autenticados podem ter acesso ao sistema, com exceção ao auto cadastramento do usuário. | Segurança | Obrigatório |
