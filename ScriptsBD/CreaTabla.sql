
# CREAR TABLAS 

create table empresa(
	ruc varchar(50),
    nombre varchar(255),
    estado varchar(50),
    departamento varchar(50),
    segmento varchar(50),
    tecnologias varchar(50),
    rango_velocidad varchar(100)
);

drop table ruc;
drop table departamento;
create table departamento(
	id int primary key auto_increment,
    nombre varchar(50)
);

drop table segmento;
create table segmento(
	id int primary key auto_increment,
    nombre varchar(50)
);
drop table estado;
create table estado(
	id int primary key auto_increment,
    nombre varchar(50)
);
drop table tecnologias;
create table tecnologias(
	id int primary key auto_increment,
    nombre varchar(50)
);

drop table rango_velocidad;
create table rango_velocidad(
	id int primary key auto_increment,
    nombre varchar(100)
);

drop table nombre_empresa;
create table nombre_empresa(
	id int primary key auto_increment,
    nombre varchar(255)
);

create table ruc(
	id int primary key auto_increment,
    nombre varchar(50),
    id_nombre_empresa int,
    foreign key(id_nombre_empresa) references nombre_empresa(id)
);

DROP TABLE IF EXISTS internet;
create table internet(
	id int primary key auto_increment,
    id_ruc int,
    id_estado int,
    id_departamento int,
    id_segmento int,
    id_tecnologias int,
    id_rango_velocidad int,
    foreign key(id_ruc) references ruc(id),
    foreign key(id_estado) references estado(id),
    foreign key(id_departamento) references departamento(id),
    foreign key(id_segmento) references segmento(id),
    foreign key(id_tecnologias) references tecnologias(id),
    foreign key(id_rango_velocidad) references rango_velocidad(id)
);
create table empresarios(
	id int primary key auto_increment,
    ruc varchar(50),
    estado varchar(50),
    departamento varchar(50),
    segmento varchar(50),
    tecnologias varchar(50),
    rango_velocidad varchar(100),
    foreign key(ruc) references ruc(nombre),
    foreign key(estado) references estado(nombre),
    foreign key(departamento) references departamento(nombre),
    foreign key(segmento) references segmento(nombre),
    foreign key(tecnologias) references tecnologias(nombre),
    foreign key(rango_velocidad) references rango_velocidad(nombre)
);
