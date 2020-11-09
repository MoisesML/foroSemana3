from flask_restful import Resource, reqparse
from models.proyecto import ProyectoModel

class ProyectosController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "nombre",
        type=str,
        required=True,
        help="Falta ingresar nombre"
    )
    parser.add_argument(
        "empresa",
        type=str,
        required=True,
        help="Falta la empresa"
    )
    parser.add_argument(
        "duracion",
        type=int,
        required=True,
        help="Falta la duracion en meses    "
    )

    def get(self):
        proyectos = ProyectoModel.query.all()
        resultado = []
        for proyecto in proyectos:
            resultado.append(proyecto.mostrar_json())
        if proyectos:
            return {
                'Confirm':True,
                'Content':resultado,
                'Message':'Estos son todos los proyectos en la API'
            }
        else:
            return {
                'Confirm':False,
                'Content':None,
                'Message':'No hay proyectos en la API'
            }

    def post(self):
        data = self.parser.parse_args()
        proyecto = ProyectoModel(data['nombre'], data['empresa'], data['duracion'])
        try:
            proyecto.guardar_datos()
            return {
                'Confirm':True,
                'Content':proyecto.mostrar_json(),
                'Message':'Proyecto creado exitosamente en la API'
            }, 201
        except:
            return {
                'Confirm':False,
                'Content':None,
                'Message':'No se pudo registrar el proyecto en la API'
            }, 400

class ProyectoController(Resource):
    def get(self, proyecto_id):
        proyecto = ProyectoModel.query.filter_by(id=proyecto_id).first()
        resultado = proyecto.mostrar_json()
        return {
            'Content':resultado
        }
