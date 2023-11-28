from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello again!'

@app.route('/formulari')
def formulari_get():
    # mostrem el formulari
    return """
<form method='post'>
    Introdueix el teu nom:
    <input name='nom' type='text' />
    <br>
    <input type='submit'>
</form>
"""
# important importar la request per accedir a les dades adjuntes
from flask import request

@app.route('/formulari', methods=['POST'])
def formulari_post():
    # processem les dades del formulari
    nom = request.form["nom"]
    return "Salut, {}".format(nom)
