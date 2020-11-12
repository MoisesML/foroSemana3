from baseDatos import db

class SkillModel(db.Model):
    __tablename__='t_skills'
    id = db.Column('skil_id', db.Integer, primary_key=True)
    nombre = db.Column('skil_nombre', db.String(20))
    valoracion  = db.Column('skil_valor', db.DECIMAL(2,1))
    person_id = db.Column(db.Integer, db.ForeignKey('t_personas.person_id'))

    def __init__(self, nombre, valoracion, person_id):
        self.nombre = nombre
        self.valoracion = valoracion
        self.person_id = person_id

    def guardar_datos(self):
        db.session.add(self)
        db.session.commit()

    def mostrar_json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'valoracion':float(self.valoracion),
            'persona':self.person_id
        }

    def __str__(self):
        return '%s, %s, %s, %s'%(self.nombre, self.valoracion, self.person_id)