create database agenda;
use agenda;
create table login(
usuario varchar(50) not null,
contrasena varchar(50) not null);

create table datosagenda(
id int not null primary key auto_increment,
nombre varchar(70) not null,
apellido varchar(70)not null,
telefono varchar(70) not null 
correo varchar(70)not null);



INSERT INTO `agenda`.`login` (`usuario`, `contrasena`) VALUES ('utec', 'utec');
