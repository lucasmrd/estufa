from peewee import Model, IntegerField, BooleanField
from database.database import db

class Estufa(Model):
    temperatura = IntegerField()
    umidade = IntegerField()
    velocidade_fan = IntegerField()
    status_lampada = BooleanField()

    class Meta:
        database = db

    def to_dict(self):
        return {
            "id": self.id,
            "temperatura": self.temperatura,
            "umidade": self.umidade,
            "velocidade_fan": self.velocidade_fan,
            "status_lampada": self.status_lampada
        }