from baseDatos import db

class PersonaModel(db.Model):
    __tablename__ = "t_personas"
    id = db.Column("person_id", db.Integer, primary_key=True)
    nombre = db.Column("person_nombre", db.String(20))
    dni = db.Column("person_dni", db.Integer)
    telefono = db.Column("person_telefono", db.String(12))
    email = db.Column("person_email", db.String(100))
    puesto = db.Column("person_puesto", db.String(50))
    proyecto = db.relationship('ProyectoModel', backref='persona')
    skills = db.relationship('SkillModel', backref='persona')

    def __init__(self, nombre, dni, telefono, email, puesto):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.puesto = puesto

    def guardar_datos(self):
        db.session.add(self)
        db.session.commit()

    def mostrar_json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'dni':self.dni,
            'telefono':self.telefono,
            'email':self.email,
            'puesto':self.puesto
        }

    def __str__(self):
        return '%s, %s, %s, %s, %s'%(self.nombre, self.dni, self.telefono, self.email, self.puesto)