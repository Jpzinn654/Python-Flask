from flask import Flask
from routes.home import home_rout

#Inicialização
app = Flask(__name__)

@app.register_blueprint(home_rout)

# Indicar que estamos no modo desenvolvedor para n encerar a aplicação a cada alteração
app.run(debug=True)