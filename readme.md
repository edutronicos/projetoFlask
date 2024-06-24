# CRUD de Cadastro de Alunos com Flask
Este projeto foi desenvolvido para a disciplina de Projeto de Software do segundo período do curso de Análise e Desenvolvimento de Sistemas. O objetivo é demonstrar um sistema CRUD (Criar, Ler, Atualizar, Deletar) de cadastro de alunos com uma interface simples e intuitiva, incluindo tela de login para acesso. O banco de dados MySQL é utilizado para armazenar os dados de usuários, logins e informações dos alunos.

## Importante: 
O sistema de login é uma simulação e não utiliza criptografia. A validação ocorre apenas comparando o usuário e senha informados com os dados cadastrados no banco de dados.

## Funcionalidades:
- Cadastro de usuários: Permite criar novos usuários no sistema.
- Login: Acesso ao menu principal do sistema após validação de usuário e senha.
- Cadastro de alunos: Criação de novos registros de alunos com nome, sexo, data de nascimento e RA.
- Atualização de cadastro: Modificação dos dados de um aluno já cadastrado.
- Listagem de alunos: Exibição de todos os alunos cadastrados no sistema.
- Pesquisa de alunos: Localização de alunos específicos por meio de critérios de busca.
- Relatório em PDF: Geração de um relatório em formato PDF contendo a lista de alunos cadastrados.
- Exclusão de usuário: Remoção de um usuário do sistema.

## Tecnologias Utilizadas
- Linguagens: HTML, CSS, Python
- Banco de dados: MySQL
- Frameworks: Flask, Bootstrap

## Bibliotecas Python
- mysql.connector: Conexão e interação com o banco de dados MySQL.
- reportlab.pdfgen e reportlab.lib.pagesizes: Geração do relatório em PDF.
- Flask: Framework web para desenvolvimento da aplicação.

## Estrutura do Banco de Dados

* Tabela usuarios
id (chave primária)
user (nome de usuário)
password (senha)
create_at (data de criação)
update_at (data de atualização)

* Tabela alunos
id (chave primária)
nome (nome do aluno)
ra (registro acadêmico)
sexo (sexo do aluno)
data_nasc (data de nascimento)
create_at (data de criação)
update_at (data de atualização)