from flask import Flask,url_for,render_template
from routes.home import home_route
from routes.cliente import cliente_route

#inicialização
app = Flask(__name__) #identificar e organizar os recursos
app.register_blueprint(cliente_route,url_prefix='/cliente')
app.register_blueprint(home_route,url_prefix='/')
app.run(debug=True) # Modo desenvolvedor
