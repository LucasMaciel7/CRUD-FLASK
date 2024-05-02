from flask import Blueprint,render_template,request
from database.models.Cliente import Cliente 

cliente_route= Blueprint('cliente',__name__)


#Lista todos clientes
@cliente_route.route('/')
def lista_clientes ():

    clientes = Cliente.select()
    print ("lista_clientes",clientes)
    return render_template("lista_clientes.html",clientes=clientes)



#Obtem os dados somente de um cliente

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente (cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html',cliente = cliente)



#Insere um novo cliente
@cliente_route.route('/',methods=['POST'])
def inserir_cliente ():
        
    data = request.json # recebe  o formulario do front 

    if data["nome"] == "" or data["email"] == "" :
        return render_template('Erro.html')

    else:
        novo_usuario = Cliente.create(
            nome=data["nome"],
            email = data["email"]       
            )
        # renderiza a pagina html passando a variavel de contexeto do cliente
        return render_template('item_cliente.html',cliente= novo_usuario)   


    
# Renderiza as informações para criar um novo cliente
@cliente_route.route('/new',methods=['GET'])
def form_cliente ():
     return render_template('form_cliente.html')


# Renderiza o formulario de edição de um cliente
@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html',cliente=cliente)

# Realiza o update das informações de um cliente
@cliente_route.route('/<int:cliente_id>/update',methods=['PUT'])
def atualizar_cliente(cliente_id):
    cliente_editado = None

    # obter dados do formulario
    data = request.json

    #obter o usuario pelo id 
    cliente_editado = Cliente.get_by_id(cliente_id)

    #Atualiza valores
    cliente_editado.nome = data["nome"]
    cliente_editado.email = data["email"]
    cliente_editado.save() 

    #Retorna front o template com a variavel de contexto
    return render_template('item_cliente.html',cliente = cliente_editado)


# Deleta um cliente do banco de dados
@cliente_route.route('/<int:cliente_id>/delete',methods=['DELETE'])
def delete_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted':'ok'}




