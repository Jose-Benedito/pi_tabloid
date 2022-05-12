from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login',  methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "esta é logout page"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nome = request.form.get('nome')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)< 4:
            flash('email deve ter mais de 4 caracteres', category='error')
        elif len(nome) < 2:
            flash(' nome deve ter mais de um caractere', category='error')
        elif len(password1) < 6:
            flash(' Senha deve ter mais de 6 caractere', category='error')
        elif (password2) != password1:
            flash('Senhas não correspondentes', category='error')
        else:
            # add user to database
            new_user = User(email=email, nome=nome, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('conta criado com sucesso!', category='success')
            return redirect(url_for('views.home'))



    return render_template('sign_up.html')