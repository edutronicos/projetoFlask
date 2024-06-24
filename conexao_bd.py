import mysql.connector
from datetime import date 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

#Validando usuário cadastrado no banco de dados.
def logar(usuario, senha):
    conexao = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        database = 'projeto',
        user = 'root',
        password = '12345'
    )
    user = usuario
    password = senha
    comando = ("SELECT * FROM usuarios WHERE user = %s AND password = %s")
    cursor = conexao.cursor(buffered=True)
    cursor.execute(comando, (user, password))
    if cursor.fetchone():
        print("Login bem-sucedido")
        return True
    else:
        print("Nome de usuário ou senha incorretos")

    cursor.close()
    conexao.close()

#Salva usuário e senha no banco de dados.
def registrar(usuario, senha):
    try:
        conexao = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            database = 'projeto',
            user = 'root',
            password = '12345'
        )
        user = usuario
        password = senha
        data = date.today()
        print(data)
        comando = ("INSERT INTO usuarios (user, password, create_at) VALUES (%s, %s, %s)")
        cursor = conexao.cursor(buffered=True)
        cursor.execute(comando, (user, password, data))
        yes = conexao.commit()

        print("Registrado com Sucesso.")
        return True
    
    except mysql.connector.Error as err:
        print('Erro ao realizar o registro: {err}')
        return False
        
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

#Salva os dados do aluno no banco de dados.
def salvar_cadastro(nome, ra, sexo, nascimento):
    try:
        conexao = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            database = 'projeto',
            user = 'root',
            password = '12345'
        )
        nome = nome
        ra = ra
        sexo = sexo
        nascimento = nascimento
        data = date.today()
        comando = ("INSERT INTO alunos (nome, ra, foto, d_nasc, create_at) VALUES (%s, %s, %s, %s, %s)")
        cursor = conexao.cursor(buffered=True)
        cursor.execute(comando, (nome, ra, sexo, nascimento, data))
        yes = conexao.commit()

        print("Registrado com Sucesso.")
        return True
    
    except mysql.connector.Error as err:
        print('Erro ao realizar o registro: {err}')
        return False
        
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

#Listar Alunos cadastrados no banco de dados.
def listar():
    conexao = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        database = 'projeto',
        user = 'root',
        password = '12345'
    )
    comando = """SELECT * FROM alunos"""
    cursor = conexao.cursor(buffered=True)
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado


#Pesquisa por alunos no banco de dados.
def pesquisar(nome='', ra=''):
    conexao = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        database = 'projeto',
        user = 'root',
        password = '12345'
    )
    nome = nome
    ra = ra
    if nome:
        comando = ("SELECT * FROM alunos WHERE nome LIKE %s ")
        cursor = conexao.cursor(buffered=True)
        cursor.execute(comando, ("%" + nome + "%", ))
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultado
    else:
        comando = ("SELECT * FROM alunos WHERE ra LIKE %s ")
        cursor = conexao.cursor(buffered=True)
        cursor.execute(comando, ("%" + ra + "%", ))
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultado


def gerar_pdf_do_banco(nome):
    conexao = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        database = 'projeto',
        user = 'root',
        password = '12345'
    )
    nome_arquivo = nome
    comando = ("SELECT nome, ra, foto, d_nasc FROM alunos")
    cursor = conexao.cursor(buffered=True)
    cursor.execute(comando)
    resultado = cursor.fetchall()
    c = canvas.Canvas(nome_arquivo, pagesize=letter)

    c.setFont("Helvetica", 20)
    c.drawString(150, 720, "Relatório de alunos cadastrados.")
    
    c.setFont("Helvetica", 12)
    y = 680  # Posição inicial vertical

    c.line(50, 710, 550, 710)
    for linha in resultado:
        x = 20  # Posição inicial horizontal
        for item in linha:
            c.drawString(x, y, str(item))
            x += 150  # Ajuste o espaçamento entre colunas
        y -= 20  # Ajuste o espaçamento entre linhas

    c.save()
    cursor.close()


#Busca usuario pelo id e retorna informações do banco de dados.
def busca_atualizar(id):
    conexao = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        database = 'projeto',
        user = 'root',
        password = '12345'
    )
    id = id
    comando = ("SELECT * FROM alunos WHERE id = %s")
    cursor = conexao.cursor(buffered=True)
    cursor.execute(comando, (id,))
    aluno = cursor.fetchone()
    if aluno:
        print(aluno)
        return aluno
    else:
        print("Ocorreu um erro na consulta.")

    cursor.close()
    conexao.close()

def atualizar_cadastro(id, nome, ra, sexo, nascimento):
    try:
        conexao = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            database = 'projeto',
            user = 'root',
            password = '12345'
        )
        id = id
        nome = nome
        ra = ra
        sexo = sexo
        nascimento = nascimento
        data = date.today()
        comando = ("UPDATE alunos set nome = %s, ra = %s, foto = %s, d_nasc = %s, update_at = %s where id = %s;")
        cursor = conexao.cursor(buffered=True)
        cursor.execute(comando, (nome, ra, sexo, nascimento, data, id))
        conexao.commit()

        print("Aluno atualizado com Sucesso.")
        return True
    
    except mysql.connector.Error as err:
        print('Erro ao atualizar aluno: {err}')
        return False
        
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def deletar(id):
    conexao = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        database = 'projeto',
        user = 'root',
        password = '12345'
    )
    id = id
    comando = ("DELETE FROM alunos WHERE id = %s")
    cursor = conexao.cursor(buffered=True)
    cursor.execute(comando, (id,))
    conexao.commit()

    cursor.close()
    conexao.close()





# logar('admin', '123')

# user = 'admin'
# senha = '123'

# sql = ("SELECT * FROM usuarios WHERE user = %s AND password = %s")

# cursor = conexao.cursor(buffered=True)
# cursor.execute(sql, (user, senha))

# if cursor.fetchone():
#     print("Login bem-sucedido")
# else:
#     print("Nome de usuário ou senha incorretos")

# print(cursor.fetchall()) # resultado da query

# if conexao.is_connected():
#     print('O yuri ta conectado')

