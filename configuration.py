from routes.home import home_route
from routes.cliente import cliente_route
from database.database import db
from database.models.Cliente import Cliente



def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(cliente_route,url_prefix='/cliente')
    app.register_blueprint(home_route,url_prefix='/')


# Realiza a configuração do Banco de dados, toda vez que rodar o projeto
def configure_db():
    db.connect()
    db.create_tables([Cliente]) # Cria uma tabela cliente, caso ja exista uma ele somente usa ela.

