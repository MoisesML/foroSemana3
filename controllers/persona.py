from flask_restful import Resource, reqparse
from models.persona import PersonaModel

class PersonasController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "nombre",
        type=str,
        required=True,
        help="Falta ingresar nombre"
    )
    parser.add_argument(
        "dni",
        type=int,
        required=True,
        help="Falta su dni"
    )
    parser.add_argument(
        "telefono",
        type=str,
        required=True,
        help="Falta su numero telefonico"
    )

    def get(self):
        personas = PersonaModel.query.all()
        busqueda = []
        for persona in personas:
            busqueda.append(persona.mostrar_json())
        return {
            'Content':busqueda
        }

    def post(self):
        data = self.parser.parse_args()
        persona = PersonaModel(data['nombre'], data['dni'], data['telefono'])
        try:
            persona.guardar_datos()
            return {
                'Confirm':True,
                'Content':persona.mostrar_json(),
                'Message':'Persona creada exitosamente en la API'
            }, 201
        except:
            return {
                'Confirm':False,
                'Content':None,
                'Message':'No se pudo registrar a la persona en la API'
            }, 400
