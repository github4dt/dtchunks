import json
from os import environ as env

from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for, request, jsonify, send_file
import requests

import boto3
import openai
import markdown

import time
from samples import sample_ac, sample_bc, sample_pe, enterprises, tb_review, tb_result_ac, tb_result_poder, enterprises_back

import random

# Flask app
app = Flask(__name__)


NAME_LIST = ['8,721 - Constitutiva.pdf', 'PODER ON TIME MOBILE TECHONOLOGIES SA DE CV A FAVOR DE FABIAN ANDRES BERDIALES (1).pdf']


# Flask routes
@app.route('/')
def index():
    return render_template('code.html')
    # return render_template('index.html')


@app.route('/info', methods=['POST'])
def info():
    # validacion de el codigo 
    code = request.form['code']
    print(code)
    
    if code == '.des':
        return render_template('upload.html')
    else:
        return render_template('code.html', error=True)

    return redirect(url_for('index'))


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    # Datos del usuario
    name = request.form['name']
    email = request.form['email']
    key = request.form['key'].upper()
    print(name, email, key)
    
    return render_template('upload.html', upload=True)


# 3 endpoints para cada Files por separado
@app.route('/upload_file', methods=['POST', 'GET'])
def upload_file():
    # verificacion de el archivo
    file = request.files['file']

    # asegurar que el archivo sea pdf
    if not file.filename.endswith('.pdf'):
        return jsonify({'status': 'error', 'message': 'El archivo debe ser PDF'})

    # (type_file = request.form['type'])
    index = request.form['index']
    print(file, index)

    # (type_list = ['Acta Constitutiva', 'Poder', 'Asamblea'])

    # (primera pagina a gpt4v)

    time.sleep(random.randint(5, 9))
    # time.sleep(1)

    if file.filename == NAME_LIST[int(index)]:
        return jsonify({'status': 'ok', 'message': '✅ El archivo se ha cargado correctamente'})
    else:
        return jsonify({'status': 'error', 'message': '❌ No coincide con el tipo de archivo'})


@app.route('/success', methods=['POST', 'GET'])
def success():
    return render_template('upload.html', success=True)


@app.route('/system/<int:id>', methods=['POST', 'GET'])
def system(id):
    if id == 0:
        return render_template('system.html', enterprises=markdown.markdown(enterprises, extensions=['tables']), employee={'name': 'Emmanuel Sánchez', 'image': '/static/img/profile.jpg'})
    if id == 1:
        return render_template('system.html', enterprises=markdown.markdown(enterprises_back, extensions=['tables']), employee={'name': 'Emmanuel Sánchez', 'image': '/static/img/profile.jpg'}, back=True)


@app.route('/review/<int:id>', methods=['POST', 'GET'])
def review(id):
    # Crear lista de la tabla Markdown
    tb_list = enterprises.split('\n')

    # Recrear la tabla Markdown con el id
    tb_new = tb_list[0] + '\n' + tb_list[1] + '\n' + tb_list[id + 2]


    enterprise_html = markdown.markdown(tb_new, extensions=['tables'])

    review_html = markdown.markdown(tb_review, extensions=['tables'])

    return render_template('review.html', id=id, enterprise=enterprise_html, review=review_html)


@app.route('/analyze/<int:id>', methods=['POST', 'GET'])
def analyze(id):
    print(id)
    tb_list = [tb_result_ac, tb_result_poder]
    # table_html = markdown.markdown(tb_list[id], extensions=['tables'])
    time.sleep(random.randint(50, 60))
    # time.sleep(1)
    return jsonify({'status': 'ok', 'table': tb_list[id]})


@app.route('/download/<int:id>', methods=['POST', 'GET'])
def download(id):
    file_path = 'static/files/' + NAME_LIST[id]
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()