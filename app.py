from flask import Flask
from flask_restful import Api
from baseDatos import db

#Importar controllers
from controllers.persona import PersonasController
from controllers.proyecto import ProyectosController, ProyectoController
from controllers.skill import SkillController
from controllers.solicitudes import SolicitudesController, SolicitudController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://s3y37k82kydfuzsx:uo2flrzhi1rzp16m@ko86t9azcob3a2f9.cbetxkdyhwsb.us-east-1.rds.amazonaws.com/ggdki8pav3lyhj0l'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/portafolio'
api = Api(app=app)

@app.before_first_request
def iniciador():
    db.init_app(app)
    db.drop_all(app=app)
    db.create_all(app=app)

@app.route("/")
def inicio():
    return 'Servidor - Foro semana 3 corriendo exitosamente'

api.add_resource(PersonasController,'/persona')
api.add_resource(ProyectosController,'/proyecto')
api.add_resource(ProyectoController,'/proyecto/<int:proyecto_id>')
api.add_resource(SkillController,'/skill')
api.add_resource(SolicitudesController,'/solicitudes')
api.add_resource(SolicitudController,'/solicitud/<int:persona>')

if __name__ == '__main__':
    app.run(debug = True)