from app.db import db

class Departamento(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    departamentos=db.relationship('Internet',backref='departamento',lazy=True)

    def __init__(self, nombre):
        self.nombre=nombre

class Segmento(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    segmentos=db.relationship('Internet',backref='segmento',lazy=True)

    def __init__(self, nombre):
        self.nombre=nombre    

class Estado(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    estados=db.relationship('Internet',backref='estado',lazy=True)

    def __init__(self, nombre):
        self.nombre=nombre    

class Tecnologias(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    tecno=db.relationship('Internet',backref='tecnologias',lazy=True)

    def __init__(self, nombre):
        self.nombre=nombre

class Rango_velocidad(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100))
    rv=db.relationship('Internet',backref='rango_velocidad',lazy=True)

    def __init__(self, nombre):
        self.nombre=nombre

class Nombre_empresa(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    rucs=db.relationship('Ruc',backref='nombre_empresa',lazy=True)

    def __init__(self, nombre):
        self.nombre=nombre

class Ruc(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50))
    id_nombre_empresa=db.Column(db.Integer,db.ForeignKey('nombre_empresa.id',ondelete='CASCADE'))
    rucc=db.relationship('Internet',backref='ruc',lazy=True)

    def __init__(self, nombre,id_nombre_empresa):
        self.nombre=nombre
        self.id_nombre_empresa=id_nombre_empresa

class Internet(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    id_ruc=db.Column(db.Integer,db.ForeignKey('ruc.id',ondelete='CASCADE'))
    id_estado=db.Column(db.Integer,db.ForeignKey('estado.id',ondelete='CASCADE'))
    id_departamento=db.Column(db.Integer,db.ForeignKey('departamento.id',ondelete='CASCADE'))
    id_segmento=db.Column(db.Integer,db.ForeignKey('segmento.id',ondelete='CASCADE'))
    id_tecnologias=db.Column(db.Integer,db.ForeignKey('tecnologias.id',ondelete='CASCADE'))
    id_rango_velocidad=db.Column(db.Integer,db.ForeignKey('rango_velocidad.id',ondelete='CASCADE'))

    def __init__(self, id_ruc,id_estado,id_departamento,id_segmento,id_tecnologias,id_rango_velocidad):
        self.id_ruc=id_ruc
        self.id_estado=id_estado
        self.id_departamento=id_departamento
        self.id_segmento=id_segmento
        self.id_tecnologias=id_tecnologias
        self.id_rango_velocidad=id_rango_velocidad
