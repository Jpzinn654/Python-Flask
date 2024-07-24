from flask import Blueprint

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
    return ('lista de clientes')

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    pass

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delte_cliente(cliente_id):
    pass