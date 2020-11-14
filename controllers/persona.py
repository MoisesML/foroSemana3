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
    parser.add_argument(
        "email",
        type=str,
        required=True,
        help="Falta su email"
    )
    parser.add_argument(
        "puesto",
        type=str,
        required=True,
        help="Falta su puesto"
    )
    parser.add_argument(
        "desc_personal",
        type=str,
        required=True,
        help="Falta su descripcion personal"
    )
    parser.add_argument(
        "desc_profesional",
        type=str,
        required=True,
        help="Falta su descripcion profesional"
    )

    def get(self):
        personas = PersonaModel.query.all()
        resultado = []
        for persona in personas:
            temporal = persona.mostrar_json()
            lista = []
            lista1 = []
            for skill in persona.skills:
                lista1.append(skill.mostrar_json())
            for proyecto in persona.proyecto:
                lista.append(proyecto.mostrar_json())
            temporal['proyectos'] = lista
            temporal['skills'] = lista1
            resultado.append(temporal)

        return {
            'Content':resultado
        }

    def post(self):
        data = self.parser.parse_args()
        persona = PersonaModel(data['nombre'], data['dni'], data['telefono'], data['email'], data['puesto'], data['desc_personal'], data['desc_profesional'])
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

class PersonaController(Resource):
    def get (self, person_id):
        persona = PersonaModel.query.filter_by(id=person_id).first()
        resultado = persona.mostrar_json()
        return {
            'Confirm':True,
            'Content':resultado,
            'Message':'Esta es la informacion de la persona con id '+str(person_id)
        }

    def put(self, person_id):
        persona = PersonaModel.query.filter_by(id=person_id).first()
        if persona:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "desc_personal",
                type=str
            )
            parser.add_argument(
                "desc_profesional",
                type=str
            )
            data = parser.parse_args()
            persona.desc_personal = data['desc_personal']
            persona.desc_profesional = data['desc_profesional']
            persona.guardar_datos()
            return {
                'Confirm':True,
                'Content':persona,
                'Message':'Se actualizo la información correctamente'
            }
        else:
            return {
                'Confirm':False,
                'Content':None,
                'Message':'No existe persona con ese id'
            }
        