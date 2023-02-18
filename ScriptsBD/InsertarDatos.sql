#INSERTAR DATOS
truncate table departamento;
#departamento
insert into departamento(nombre)
select distinct departamento from empresa;

#segmento
truncate table segmento;
insert into segmento(nombre)
select distinct segmento from empresa;
select * from segmento;

select * from nombre_empresa;
#estado
truncate table estado;
insert into estado(nombre)
select distinct estado from empresa;
select * from estado;

#tecnologicas
truncate table tecnologias;
insert into tecnologias(nombre)
select distinct tecnologias from empresa;
select * from tecnologias;


#rango_velocidad
truncate table rango_velocidad;
select distinct rango_velocidad from empresa;
insert into rango_velocidad(nombre)
select distinct rango_velocidad from empresa;
select * from rango_velocidad;

#nombre_empresa
truncate table nombre_empresa;
insert into nombre_empresa(nombre)
select distinct nombre from empresa;
select * from nombre_empresa;

#ruc
delete from empresa where ruc="";


insert into ruc(nombre,id_nombre_empresa)
(
select distinct a.ruc,b.id from empresa a join nombre_empresa b on a.nombre=b.nombre
);

#Internet
insert into internet(id_ruc,id_estado,id_departamento,id_segmento,id_tecnologias,id_rango_velocidad)
(
select ne.id as id_ruc ,e.id as id_estado,d.id as id_departamento,s.id as id_segmento,t.id as id_tecnologias,r.id as id_rango_velocidad
from empresa a 
join ruc ne 
on a.ruc=ne.nombre

join estado e 
on a.estado=e.nombre
join departamento d
on a.departamento=d.nombre
join segmento s
on a.segmento=s.nombre
join tecnologias t
on a.tecnologias=t.nombre
join rango_velocidad r
on a.rango_velocidad=r.nombre
);




