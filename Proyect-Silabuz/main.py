from app import create_app
from flask_marshmallow import Marshmallow
import json
from flask import render_template,redirect,url_for
from flask import request,jsonify
from app.db import db
from app.models.Internet import Departamento,Segmento,Tecnologias,Rango_velocidad,Nombre_empresa,Estado,Ruc,Internet
#from flask_restful import Api, Resource

app=create_app()
ma = Marshmallow(app) #Es una extensión que facilita la 
#serialización de los modelos de la base de datos a JSON y viceversa
#api = Api(app) # new

#Schema de salon
class DepartamentoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')
        model =Departamento

departamento_schema = DepartamentoSchema() 
departamento_schema = DepartamentoSchema(many=True)

class SegmentoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')
        model =Segmento

segmento_schema = SegmentoSchema() 
segmento_schema = SegmentoSchema(many=True)


class TecnologiasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')
        model =Tecnologias

tecnologias_schema = TecnologiasSchema() 
tecnologias_schema = TecnologiasSchema(many=True)


class Rango_velocidadSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')
        model =Rango_velocidad

rango_velocidad_schema = Rango_velocidadSchema() 
rango_velocidad_schema = Rango_velocidadSchema(many=True)


class Nombre_empresaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')
        model =Nombre_empresa

nombre_empresa_schema = Nombre_empresaSchema() 
nombre_empresa_schema = Nombre_empresaSchema(many=True)

class EstadoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')
        model =Estado

estado_schema = EstadoSchema() 
estado_schema = EstadoSchema(many=True)

class RucSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre','id_nombre_empresa')
        model =Ruc

ruc_schema = RucSchema() 
ruc_schema = RucSchema(many=True)

class InternetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_ruc','id_estado','id_departamento','id_segmento','id_tecnologias','id_rango_velocidad')
        model =Internet

internet_schema = InternetSchema() 
internet_schema = InternetSchema(many=True)


@app.route('/',) #ruta raiz
def index():
    return render_template('index.html')


    

@app.route('/ver-segmento',methods=['GET']) #ruta raiz
def ver_segmento():
    segmento = Segmento.query.all()
    if segmento:
        return segmento_schema.dump(segmento)
    return {"message": ("No hay aulas registradas")}

#api.add_resource(add_salones, '/salones')
@app.route('/ver-internet',methods=['GET']) #ruta raiz
def ver_internet():
    internets = Internet.query.all()
    if internets:
        return internet_schema.dump(internets)
    return {"message": ("No hay aulas registradas")}


@app.route('/ver/<id>',methods=['GET']) #ruta raiz
def ver_algo(id):
    ruc=Nombre_empresa.query.filter_by(id=id)
    #departamento=Departamento.query.filter_by(nombre=nombre).all()
    return nombre_empresa_schema.jsonify(ruc)
    
""" class Test(Resource):
    @classmethod
    def get(cls, id: int):
        test = Salon.query.filter_by(id=id).all()
        #db.session.query()
        #Salon.query.filter_by(id=id).first_or_404()
        if test:
            return salon_schema.dump(test), 200
        return {"message": ("test_test_not_found")}, 404 """






#Ver por salon
"""@app.route('/ver-salones/<id>', methods=['GET'])
def get_salones_id(id):
                        #WHERE
    salon =Salon.query.filter_by(id=id).all()
    if salon:
        return salon_schema.dump(salon), 200
    return {"message": ("Aula no encontrada")}, 404

#api.add_resource(get_salones_id, "/ver-salones/<id>", endpoint='test-api')

@app.route('/salon/<id>', methods=['DELETE'])
def delete_salon(id):

    salon = Salon.query.get(id)
    db.session.delete(salon)
    db.session.commit()
    return {"message": ("Aula eliminada")}, 200

@app.route('/salon-update/<id>', methods=['PUT'])
def update_salon(id):
        
    salon = Salon.query.get(id)
    aula=request.json['aula']
    hora_entrada=request.json['hora_entrada']

    salon.aula = aula
    salon.hora_entrada = hora_entrada
    db.session.commit()

    return {"message": ("Aula Actualizada")}, 200

#
@app.route('/salon-update-path/<id>', methods=['PATCH'])
def update_salon_path(id):
        
    salon = Salon.query.get(id)
    aula=request.json['aula']
    #hora_entrada=request.json['hora_entrada']



    salon.aula = aula
    #salon.hora_entrada = hora_entrada
    db.session.commit()

    return {"message": ("Aula Actualizada")}, 200 """





db.init_app(app)
with app.app_context():
    db.create_all()
    #print("BD conectada!") 

if __name__ == "__main__":
    app.run(debug=True)
