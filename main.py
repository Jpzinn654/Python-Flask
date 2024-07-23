from flask import Flask, render_template

#Inicialização
app = Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
    titulo = 'Página Inicial'
    usuario = [
        {'nome': 'Guilherme', 'membro_ativo': True},
        {'nome': 'Joao', 'membro_ativo': False},
        {'nome': 'Maria', 'membro_ativo': False},
    ]
    return render_template('index.html', titulo=titulo, usuario=usuario)

# Indicar que estamos no modo desenvolvedor para n encerar a aplicação a cada alteração
app.run(debug=True)

