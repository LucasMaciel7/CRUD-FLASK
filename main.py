from flask import Flask,url_for,render_template
from configuration import configure_all

#inicialização
app = Flask(__name__) #identificar e organizar os recursos

configure_all(app)

app.run(debug=True) # Modo desenvolvedor


