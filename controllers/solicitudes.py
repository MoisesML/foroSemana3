from flask_restful import Resource, reqparse
from models.solicitudes import SolicitudesModel

class SolicitudesController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "nombre",
        type=str,
        required=True,
        help='Ingrese su nombre'
    )
    parser.add_argument(
        "email",
        type=str,
        required=True,
        help='Ingrese su correo'
    )
    parser.add_argument(
        "telefono",
        type=int,
        required=True,
        help='Ingrese su numero telefonico'
    )
    parser.add_argument(
        "mensaje",
        type=str,
        required=True,
        help='Ingrese su mensaje'
    )
    parser.add_argument(
        "person_id",
        type=str,
        required=True,
        help='Ingrese el id de la persona'
    )

    def post(self):
        data = self.parser.parse_args()
        solicitud = SolicitudesModel(data['nombre'], data['email'], data['telefono'], data['mensaje'], data['person_id'])
        try:
            solicitud.guardar_datos()
            return {
                'Confirm':True,
                'Content':solicitud.mostrar_json(),
                'Message':'La solicitud fue registrada correctamente'
            }, 201
        except:
            return {
                'Confirm':False,
                'Content':None,
                'Message':'La solicitud no se registro'
            }

class SolicitudController(Resource):
    def get(self, persona):
        solicitudes = SolicitudesModel.query.filter_by(person_id=persona).all()
        if solicitudes:
            lista = []
            for solicitud in solicitudes:
                lista.append(solicitud.mostrar_json())
            return {
                'Content':lista
            }
        else:
            return {
                'Confirm':False,
                'Content':None,
                'Message':'No hay solicitudes hasta ahora'
            }