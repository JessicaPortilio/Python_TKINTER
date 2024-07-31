import sqlite3
# import mysql.connector

# Função para conectar ao banco de dados e criar a tabela se ela não existir
def conectar():
    # Conecta ao banco de dados
    conexao = sqlite3.connect('pessoas.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    # Cria uma tabela chamada 'pessoa' com as colunas, se a tabela já existir, o comando não faz nada
    curso.execute('''
                CREATE TABLE IF NOT EXISTS pessoa (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    idade INTEGER,
                    email TEXT
                )
                ''')
    # Confima as mudanças no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()

# Função para inserir uma nova pessoa no banco de dados
def inserir_pessoa(nome, idade, email):
    # Conecta ao banco de dados
    conexao = sqlite3.connect('pessoas.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    
    # Inserindo uma nova linha na tabela 'pessoa' com os valores fornecidos para nome, idade, email
    curso.execute('INSERT INTO pessoa (nome, idade, email) VALUES (?, ?, ?)', (nome, idade, email))
    
    # Confima as mudanças no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()

# Função para atualizar as informações de uma pessoa no banco de dados
def atualizar_pessoa(id_pessoa, nome, idade, email):
    # Conecta ao banco de dados
    conexao = sqlite3.connect('pessoas.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    
    curso.execute('UPDATE pessoa SET nome = ?, idade = ?, email = ? WHERE id = ?', (nome, idade, email, id_pessoa))
    
    # Confima as mudanças no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()

# Função para deletar uma pessoa do banco de dados
def deletar_pessoa(id_pessoa):
    # Conecta ao banco de dados
    conexao = sqlite3.connect('pessoas.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    
    curso.execute('DELETE FROM pessoa WHERE id = ?', (id_pessoa,))
    
    # Confima as mudanças no banco de dados
    conexao.commit()
    # Fecha a conexão com o banco de dados
    conexao.close()

# Função para pesquisar pessoas no banco de dados pelo nome
def pesquisar_pessoa(nome):
    # Conecta ao banco de dados
    conexao = sqlite3.connect('pessoas.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    
    # Seleciona todas as linhas da tabela pessoa onde nome é igual nome fornecido
    curso.execute('SELECT * FROM pessoa WHERE nome = ?', (nome, ))
    # Busca todas as linhas corerspondentes e armazena na váriavel 'linhas
    linhas = curso.fetchall()
    
    # Fecha a conexão com o banco de dados
    conexao.close()
    
    # Retorna a lista de linhas encontradas
    return linhas

# Função para listar todas as pessoas no banco de dados
def lista_as_pessoas():
    # Conecta ao banco de dados
    conexao = sqlite3.connect('pessoas.db')
    # Cria um cursor para executar comandos SQL no banco de dados
    curso = conexao.cursor()
    
    # Seleciona todas as linhas da tabela 'pessoa'
    curso.execute('SELECT * FROM pessoa')
    # Busca todas as linhas  e armazena na váriavel 'linhas
    linhas = curso.fetchall()
    
    # Fecha a conexão com o banco de dados
    conexao.close()
    
    # Retorna a lista de todas as pessoas
    return linhas



