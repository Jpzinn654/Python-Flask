from flask import Blueprint, render_template, request
from database.cliente import CLIENTE

"""
Rota clientes 

 - /clientes/ (GET): Listar todos os clientes
 - /clientes/ (POST): Cadastrar um novo cliente
 - /clientes/new (GET): Formulário para cadastrar um novo cliente
 - /clientes/id (GET): Exibir um cliente específico
 - /clientes/id/edit (GET): Formulário para editar um cliente
 - /clientes/id/updade (PUT): Atualizar um cliente
 - /clientes/id/delete (DELETE): Deletar um cliente

"""

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTE)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json

    novo_usuario = {
        'id': len(CLIENTE) + 1,
        'nome': data['nome'],
        'email': data['email'],
    }

    CLIENTE.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html') 

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html') 

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    pass