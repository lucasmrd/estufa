from routes.estufa import estufa_route
from database.database import db
from database.models.estufa import Estufa

def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(estufa_route, url_prefix='/estufa')

def configure_db():
    db.connect()
    db.create_tables([Estufa])