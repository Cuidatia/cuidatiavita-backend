use cuidatiavitadb;
create table organizaciones (
	`id` int NOT NULL auto_increment,
    `nombre` varchar(100) NOT NULL,
    primary key (`id`)
);

create table usuarios(
	`id` int NOT NULL auto_increment,
    `nombre` varchar(100) null,
    `email` varchar(50) NOT NULL,
    `password` varchar(255) NOT NULL,
    `idOrganizacion` int not null,
    primary key(`id`),
    constraint FK_UsuarioOrganizacion foreign key (`idOrganizacion`) references organizaciones(`id`) 
		on delete cascade
        on update cascade,
    unique key `email` (`email`)
);

create table roles(
	`id` int not null auto_increment,
    `nombre` varchar(50) not null,
    `descripcion` varchar(255) null,
    primary key (`id`)
);

create table usuario_roles(
	`idUsuario` int not null,
    `idRol` int not null,
    primary key (`idUsuario`, `idRol`),
    constraint FK_UsuarioRolesUsuario foreign key (`idUsuario`) references usuarios(`id`)
		on delete cascade
        on update cascade,
	constraint FK_UsuarioRolesRol foreign key (`idRol`) references roles(`id`)
		on delete cascade
        on update cascade
);

create table pacientes (
	`id` int not null auto_increment,
    `nombre` varchar(100) not null,
    `primerApellido` varchar(100) not null,
    `segundoApellido` varchar(100) not null,
    `alias` varchar(50) not null,
    `fechaNaciemiento` date not null,
    `direccion` varchar(100) not null,
    `localidad` varchar(100) not null,
    `nacionalidad` varchar(50) not null,
    `genero` enum('M','F','O') not null,
    `estadoCivil` enum('ST','C', 'V', 'S', 'D') not null,
    `idOrganizacion` int not null,
    `imgPerfil` varchar(255) null,
    primary key (`id`),
    constraint FK_PacienteOrganizacion foreign key (`idOrganizacion`) references organizaciones(`id`)
		on delete cascade
        on update cascade
);

create table imagenes(
    `id` int not null auto_increment,
    `url` varchar(255) not null,
    `idPaciente` int not null,
    primary key (`id`),
    constraint FK_ImagenPaciente foreign key (`idPaciente`) references pacientes(`id`)
        on delete cascade
        on update cascade
);

create table paciente_personalReferencia(
	`idPaciente` int not null,
    `idUsuario` int not null,
    primary key (`idPaciente`, `idUsuario`),
    constraint FK_PersonalPacientePaciente foreign key (`idPaciente`) references pacientes(`id`)
		on delete cascade
        on update cascade,
    constraint FK_PersonalPacienteUsuario foreign key (`idUsuario`) references usuarios(`id`)
);

insert into organizaciones (`nombre`) values ('Cuidatia Vita');
insert into organizaciones (`nombre`) values ('Organización Prueba');

insert into usuarios (`nombre`, `email`, `password`, `idOrganizacion`) values ('Super Administrador', 'superadmin@prueba.es', '$2b$04$dqs/eS//BaJToUN9Fzg8SuvnxVEZ7yrpH5hHTV4ZPFIV0eBbFQ0Tq', 1);
insert into usuarios (`nombre`, `email`, `password`, `idOrganizacion`) values ('Administrador', 'admin@prueba.es', '$2b$04$dqs/eS//BaJToUN9Fzg8SuvnxVEZ7yrpH5hHTV4ZPFIV0eBbFQ0Tq', 2);

insert into roles (`nombre`) values ('superadmin');
insert into roles (`nombre`) values ('admin');
insert into roles (`nombre`) values ('medico');
insert into roles (`nombre`) values ('enfermero');
insert into roles (`nombre`) values ('trabajador social');
insert into roles (`nombre`) values ('terapeuta');
insert into roles (`nombre`) values ('fisioterapeuta');
insert into roles (`nombre`) values ('logopeda');
insert into roles (`nombre`) values ('auxiliar');
insert into roles (`nombre`) values ('profesional de referencia');
insert into roles (`nombre`) values ('familiar');

insert into usuario_roles (`idUsuario`, `idRol`) values (1, 1); 
insert into usuario_roles (`idUsuario`, `idRol`) values (2, 2); 