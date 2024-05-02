from peewee import Model,CharField,DateTimeField
from database.database import db
import datetime

# Cria uma Classe instanciando uma 
class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now)
    

    class Meta:
        database = db # This model uses the "people.db" database.





