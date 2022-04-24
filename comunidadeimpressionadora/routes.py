from flask import render_template, request, flash, url_for, redirect
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuarios

lista_usuarios = ['Bruno', 'Luana', 'Lucas', 'Divino']

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'login bem sucedido no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('inicio'))
        # sucesso no login, levando em consideração o botão clicado

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:

        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuarios(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()

        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
        # conta criada com sucesso, levando em consideração o botão clicado
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)
