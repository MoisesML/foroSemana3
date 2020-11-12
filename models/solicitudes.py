from baseDatos import db

class SolicitudesModel(db.Model):
    __tablename__ = 't_solicitudes'
    id = db.Column("sol_id", db.Integer, primary_key=True)
    nombre = db.Column("sol_nombre", db.String(30))
    email = db.Column("sol_email", db.String(50))
    telefono = db.Column("sol_telefono", db.String(12))
    mensaje = db.Column("sol_mensaje", db.Text)
    person_id = db.Column(db.Integer, db.ForeignKey('t_personas.person_id'))

    def __init__(self, nombre, email, telefono, mensaje, person_id):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.mensaje = mensaje
        self.person_id = person_id

    def guardar_datos(self):
        db.session.add(self)
        db.session.commit()

    def mostrar_json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'email':self.email,
            'telefono':self.telefono,
            'mensaje':self.mensaje,
            'persona':self.person_id
        }

    def __str__(self):
        return '%s, %s, %s, %s, %s'%(self.nombre, self.email, self.telefono, self.mensaje, self.person_id)