from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify, abort
from flask_login import login_required, current_user 
from .models import Note

from . import db
import json

import os

"""
    Como o arquivo estará em binario será necessário essa lib para salvar
"""
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
#@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note está muito curto', category='error')
        else:
            new_note = Note(data = note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note adicionado', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/admin')
@login_required
def admin():
    return render_template("admin.html", user=current_user)


@views.route('/cadastro')
def teste():
    return render_template("cadastro.html", user=current_user)




#Googlemaps
class Comercio:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

# AS coordenadas do endereço
comercios = (
    Comercio('mercadoA',      'Mercadinho A',  -23.571319422733524, -46.414629246163614),
    Comercio('mercadoB', 'Mercadinho B',           -23.591198056010676, -46.403604962487194),
    Comercio('mercadoC',     'Mercadinho C', -23.588869063417768, -46.40864850869)
)
comercios_by_key = {comercio.key: comercio for comercio in comercios}

 #endpoints dos mercados
@views.route('/mercadoa' )
def mercadoa ():
    return render_template("mercadoa.html", user=current_user)


@views.route ( '/mercadob' )
def  mercadob ():
    return  render_template ( "mercadob.html" ,comercios=comercios,  user = current_user  )

@views.route( '/mercadoc' )
def  mercado ():
    return  render_template ( "mercadoc.html" , user = current_user )

#GoogleMaps
@views.route("/<comercio_code>")
def show_comercio(comercio_code):
    comercio = comercios_by_key.get(comercio_code)
    if comercio:
        return render_template('map.html', comercio=comercio)
    else:
        abort(404)




@views.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST': 
        file = request.files['imagem']
        savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(savePath)
        flash('Upload Efetuado Com Sucesso', category='success')
    return render_template ( "upload.html" , user = current_user )


