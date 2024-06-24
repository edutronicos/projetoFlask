from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import conexao_bd as conex


app = Flask(__name__)
app.secret_key = b'a secret key'

# Rota para a página de login
@app.route('/')
def login():
    return render_template('login.html')

# Rota para a página inicial
@app.route('/index')
def index():
    return render_template('index.html')

# Rota para realizar o LOGIN do usuário
@app.route('/login', methods = ['GET', 'POST'])
def login_in():
    if request.method == 'POST':
        user = request.form['email']
        senha = request.form['password']
        yes = conex.logar(user, senha)
        if yes == True:
            return render_template('index.html')
        else:
            flash('Usuário ou senha incorretos.', 'error')
            return render_template('login.html')
    return render_template('login.html')


#Rota para realizar o cadastro de um novo usuário
@app.route('/login_reg', methods = ['GET', 'POST'])
def login_reg():
    if request.method == 'POST':
        user = request.form['email']
        senha = request.form['password']
        senha2 = request.form['password2']
        if senha != senha2:
            flash('As senhas precisam ser iguais.', 'error')
            return render_template('login_reg.html')
        if conex.registrar(user, senha):
            flash('Usuario cadastrado com sucesso.', 'success')
            return render_template('login.html')
        else:
            flash('Houve um problema com seu cadastro.', 'error')
            return render_template('login_reg.html')
    return render_template('login_reg.html')

#Realiza o cadastro de um aluno
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        ra = request.form['ra']
        sexo = request.form['sexo']
        nascimento = request.form['nascimento']
        if conex.salvar_cadastro(nome, ra, sexo, nascimento):
            flash('Aluno cadastrado com sucesso.', 'success')
            return render_template('cadastro.html')
        else:
            flash('Houve um problema ao cadastrar um novo aluno.', 'error')
            return render_template('cadastro.html')
    return render_template('cadastro.html')

#Listar os alunos cadastrados
@app.route('/lista')
def lista():
    resultado = conex.listar()
    # return redirect(url_for('lista', alunos=alunos))
    return render_template('lista.html', alunos=resultado)

# Realiza uma busca por alunos no banco de dados.
@app.route('/pesquisar', methods=['GET', 'POST'])
def pesquisar():
    if request.method == 'POST':
        nome = request.form['nome']
        ra = request.form['ra']
        resultado = conex.pesquisar(nome, ra)
        if resultado:
            return render_template('pesquisar.html', aluno=resultado)
        else:
            return render_template('pesquisar.html', error='Veículo não encontrado')
    return render_template('pesquisar.html')

# Rota para gerar um PDF com os dados do banco de dados.
@app.route('/gerar')
def gerar():
    conex.gerar_pdf_do_banco('alunos.pdf')
    path = 'alunos.pdf'
    return send_file(path, as_attachment=True)


# Rota para atualizar os dados de um aluno.
@app.route('/atualizar/<id>', methods=['GET', 'POST'])
def atualizar(id):
    aluno = conex.busca_atualizar(id)
    
    if request.method == 'POST':
        nome = request.form['nome']
        ra = request.form['ra']
        sexo = request.form['sexo']
        nascimento = request.form['nascimento']
        conex.atualizar_cadastro(id, nome, ra, sexo, nascimento)
        return redirect(url_for('lista'))
    return render_template('update.html', aluno = aluno)

# Rota para deletar um aluno do banco de dados.
@app.route('/deletar/<id>', methods=['GET', 'POST'])
def deletar_aluno(id):
    conex.deletar(id)
    return redirect(url_for('lista'))



if __name__ == '__main__':
    app.run(debug=True)
