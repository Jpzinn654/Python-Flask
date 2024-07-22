from flask import Flask, render_template

#Inicialização
app = Flask(__name__)

#rotas
@app.route('/')
def ola_mundo():
    titulo = 'Página Inicial'
    usuario = [
        {'Nome': 'Guilherme', 'Membro ativo': True},
        {'Nome': 'Joao', 'Membro ativo': False},
        {'Nome': 'Maria', 'Membro ativo': False},
    ]
    return render_template('index.html', titulo=titulo, usuario=usuario)

# Indicar que estamos no modo desenvolvedor para n encerar a aplicação a cada alteração
app.run(debug=True)

