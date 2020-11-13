from flask_restful import Resource, reqparse
from models.skill import SkillModel

class SkillsController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "nombre",
        type=str,
        required=True,
        help='Ingrese el nombre de la skill'
    )
    parser.add_argument(
        "valoracion",
        type=float,
        required=True,
        help='Ingrese la valoracion de la skill'
    )
    parser.add_argument(
        "descripcion",
        type=str,
        required=True,
        help='Ingrese la descripcion de la skill'
    )
    parser.add_argument(
        "person_id",
        type=int,
        required=True,
        help='Ingrese el id de la persona'
    )

    def get(self):
        skills = SkillModel.query.all()
        resultado = []
        for skill in skills:
            parcial = skill.mostrar_json()
            parcial['persona'] = skill.persona.mostrar_json()
            resultado.append(parcial)
        if skills:
            return {
                'Confirm':True,
                'Content':resultado,
                'Message':'Estos son todos los skils en la API'
            }
        else:
            return {
                'Confirm':False,
                'Content':None,
                'Message':'No hay skils en la API'
            }

    def post(self):
        data = self.parser.parse_args()
        skill = SkillModel(data['nombre'], data['valoracion'], data['descripcion'] , data['person_id'])
        try:
            skill.guardar_datos()
            return {
                'Confirm':True,
                'Content':skill.mostrar_json(),
                'Message':'Skill asignada correctamente'
            }, 201
        except:
            return {
                'Confirm':False,
                'Content':None,
                'Message':'No se pudo asignar la skill'
            }, 400

class SkillController(Resource):
    def get(self, persona):
        skills = SkillModel.query.filter_by(person_id=persona)
        resultado = []
        for skill in skills:
            resultado.append(skill.mostrar_json())
        return {
            'Content':resultado
        }
