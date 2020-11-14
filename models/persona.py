from baseDatos import db

class PersonaModel(db.Model):
    __tablename__ = "t_personas"
    id = db.Column("person_id", db.Integer, primary_key=True)
    nombre = db.Column("person_nombre", db.String(20))
    dni = db.Column("person_dni", db.Integer)
    telefono = db.Column("person_telefono", db.String(12))
    email = db.Column("person_email", db.String(100))
    direccion = db.Column("person_direccion", db.Text)
    puesto = db.Column("person_puesto", db.String(50))
    desc_personal = db.Column("person_descper", db.Text)
    desc_profesional = db.Column("person_descpro", db.Text)
    proyecto = db.relationship('ProyectoModel', backref='persona')
    skills = db.relationship('SkillModel', backref='persona')

    def __init__(self, nombre, dni, telefono, email, direccion, puesto, desc_personal, desc_profesional):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.puesto = puesto
        self.desc_personal = desc_personal
        self.desc_profesional = desc_profesional

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
            'direccion':self.direccion,
            'puesto':self.puesto,
            'desc_personal':self.desc_personal,
            'desc_profesional':self.desc_profesional
        }

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s'%(self.nombre, self.dni, self.telefono, self.email, self.direccion, self.puesto, self.desc_personal, self.desc_profesional)