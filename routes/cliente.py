from flask import Blueprint,render_template,request
from database.cliente import clientes

cliente_route= Blueprint('cliente',__name__)


#Lista todos clientes
@cliente_route.route('/')
def lista_clientes ():
    return render_template("lista_clientes.html",clientes=clientes)

#Obtem os dados somente de um cliente
@cliente_route.route('/<int:cliente_id>',methods= ['GET'])
def detalhe_cliente (client_id):
    return render_template("detalhe_cliente.html")

#Insere um novo cliente
@cliente_route.route('/',methods=['POST'])
def inserir_cliente ():
        
    data = request.json # recebe  o formulario do front
    novo_usuario = {
        "id": len(clientes) + 1,
        "nome":data["nome"],
        "email":data["email"]
    }

    clientes.append(novo_usuario)

    # renderiza a pagina html passando a variavel de contexeto do cliente
    return render_template('item_cliente.html',cliente= novo_usuario)   
    
# Renderiza as informações para criar um novo cliente
@cliente_route.route('/new',methods=['GET'])
def form_cliente ():
    return render_template('form_cliente.html')


# Renderiza o formulario de edição de um cliente
@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):

    cliente = None

    for c in clientes:
        if c['id'] == cliente_id:
            cliente = c

    return render_template('form_cliente.html',cliente=cliente)

# Realiza o update das informações de um cliente
@cliente_route.route('/<int:cliente_id>/update',methods=['PUT'])
def atualizar_cliente(cliente_id):
    cliente_editado = None
    # obter dados do formulario de edição
    data = request.json

    #obter o usuario pelo id 
    for c in clientes :
        if c['id']==cliente_id:
            c['nome'] == data['nome']
            c['email'] == data['email']
            cliente_editado = c  

    # editar usuario
    return render_template('item_cliente.html',cliente = cliente_editado)


# Deleta os dados de um, cliente
@cliente_route.route('/<int:cliente_id>/delete',methods=['DELETE'])
def delete_cliente(cliente_id):
    global clientes
    clientes = [ c for c in clientes if c['id'] != cliente_id]
    return {'deleted':'ok'}




@cliente_route.route('/<int:cliente_id>/edit',methods=['PUT'])
def deletar_cliente(client_id):
    pass