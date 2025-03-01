from flask import render_template, request, url_for
import requests
from mac import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pesquisa', methods=['POST', 'GET'])
def pesquisa():
    vendor = None  # Inicializando vendor para evitar erros
    pesquisa = None  # Inicializando pesquisa para uso posterior

    if request.method == 'POST':
        pesquisa = request.form.get('pesquisa')  # Obtendo o valor do campo de pesquisa

        # Verifica se o campo de pesquisa está vazio
        if not pesquisa.strip():  # .strip() remove espaços em branco extras
            vendor = "Escreva um MAC"
        else:
            url = f"https://api.macvendors.com/{pesquisa}"
            response = requests.get(url)

            # Verificando o status da resposta
            if response.status_code == 200:
                vendor = response.text
            elif response.status_code == 404:
                vendor = "Not found"
            else:
                vendor = "Mac inválido"

    # Renderiza o template com as variáveis
    return render_template('index.html', vendor=vendor, pesquisa=pesquisa)



@app.errorhandler(404)
def page_not_fouder(e):
    return render_template('notfound.html')