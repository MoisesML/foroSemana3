from baseDatos import db

class ProyectoModel(db.Model):
    __tablename__ = "t_proyectos"
    id = db.Column("proyecto_id", db.Integer, primary_key=True)
    nombre = db.Column("proyecto_nombre", db.String(50))
    empresa = db.Column("proyecto_empresa", db.String(50))
    duracion = db.Column("proyecto_duracion", db.Integer)

    def __init__(self, nombre, empresa, duracion):
        self.nombre = nombre
        self.empresa = empresa
        self.duracion = duracion

    def guardar_datos(self):
        db.session.add(self)
        db.session.commit()

    def mostrar_json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'empresa':self.empresa,
            'duracion':self.duracion
        }

    def __str__(self):
        return '%s, %s, %s'%(self.nombre, self.empresa, self.duracion)