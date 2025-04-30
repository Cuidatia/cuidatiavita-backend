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
    `description` varchar(255) not null,
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
    `name` varchar(100) not null,
    `firstSurname` varchar(100) not null,
    `secondSurname` varchar(100) not null,
    `alias` varchar(50) not null,
    `birthDate` date not null,
    `age` int not null,
    `birdPlace` varchar(100) not null,
    `nacionality` varchar(50) not null,
    `gender` enum('M','F','O') not null,
    `address` varchar(100) not null,
    `maritalStatus` enum('ST','C', 'V', 'S', 'D') not null,
    `language` varchar(20) not null,
    `otherLanguages` varchar(50) not null,
    `culturalHeritage` varchar(255) not null,
    `faith` varchar(100) not null,
    `idOrganizacion` int not null,
    primary key (`id`),
    constraint FK_PacienteOrganizacion foreign key (`idOrganizacion`) references organizaciones(`id`)
		on delete cascade
        on update cascade
);

create table lifeStory(
	`id` int not null auto_increment,
    `idChilhood` int,
    `idYouth` int,
    `idAdulthood` int,
    `maturity` int,
    `idPaciente` int,
	primary key (`id`),
    constraint FK_PacienteLifeStory foreign key (`idPaciente`) references pacientes(`id`)
);

create table chilhood(
`id` int not null auto_increment,
`chilhoodStudy` varchar(100),
`chilhoodSchool` varchar(100),
`chilhoodMotivations`varchar(100),
`chilhoodFamilyCore` varchar(100),
`chilhoodFriendsGroup` varchar(100),
`chilhoodTravels` varchar(100),
`chilhoodFavouritePlace` varchar(100),
`chilhoodPositiveExperiences` varchar(255),
`chilhoodNegativeExperiences` varchar(255),
`chilhoodAddress` varchar(100),
`chilhoodLikes` varchar(100),
`chilhoodAfraids` varchar(100),
`idLifeStory` int,
primary key (`id`),
constraint FK_LifeStoryChilhood foreign key (`idLifestory`) references lifeStory(`id`)
);

create table youth (
    `id` int not null auto_increment,
    `youthStudy` varchar(100),
    `youthSchool` varchar(100),
    `youthMotivations` varchar(100),
    `youthFamilyCore` varchar(100),
    `youthFriendsGroup` varchar(100),
    `youthTravels` varchar(100),
    `youthFavouritePlace` varchar(100),
    `youthPositiveExperiences` varchar(255),
    `youthNegativeExperiences` varchar(255),
    `youthAddress` varchar(100),
    `youthLikes` varchar(100),
    `youthAfraids` varchar(100),
    `idLifeStory` int,
    primary key (`id`),
    constraint FK_LifeStoryYouth foreign key (`idLifeStory`) references lifeStory(`id`)
);

create table adulthood (
    `id` int not null auto_increment,
    `adulthoodStudy` varchar(100),
    `adulthoodWork` varchar(100),
    `adulthoodMotivations` varchar(100),
    `adulthoodFamilyCore` varchar(100),
    `adulthoodFriendsGroup` varchar(100),
    `adulthoodTravels` varchar(100),
    `adulthoodFavouritePlace` varchar(100),
    `adulthoodPositiveExperiences` varchar(255),
    `adulthoodNegativeExperiences` varchar(255),
    `adulthoodAddress` varchar(100),
    `adulthoodHobbies` varchar(100),
    `adulthoodAfraids` varchar(100),
    primary key (`id`)
);

create table maturity (
    `id` int not null auto_increment,
    `grandchildrenMaturity` varchar(100),
    `maturityWork` varchar(100),
    `maturityMotivations` varchar(100),
    `maturityFamilyCore` varchar(100),
    `maturityFriendsGroup` varchar(100),
    `maturityTravels` varchar(100),
    `maturityFavouritePlace` varchar(100),
    `maturityPositiveExperiences` varchar(255),
    `maturityNegativeExperiences` varchar(255),
    `maturityAddress` varchar(100),
    `maturityHobbies` varchar(100),
    `maturityAfraids` varchar(100),
    primary key (`id`)
);

create table personality (
    `id` int not null auto_increment,
    `rhythm` varchar(100),
    `habits` varchar(100),
    `desires` varchar(255),
    `admiredModels` varchar(255),
    `hobby` varchar(100),
    `fears` varchar(100),
    `goals` varchar(255),
    `idPaciente` int not null,
    primary key (`id`),
    constraint FK_PersonalityPaciente foreign key (`idPaciente`) references pacientes(`id`)
);

create table contactData (
    `id` int not null auto_increment,
    `contactName` varchar(100),
    `contactSurname` varchar(100),
    `contactAddress` varchar(100),
    `contactEmail` varchar(100),
    `contactPhone` varchar(20),
    `idPaciente` int not null,
    primary key (`id`),
    constraint FK_ContactPaciente foreign key (`idPaciente`) references pacientes(`id`)
);

create table mainSanitaryData (
    `id` int not null auto_increment,
    `mainIllness` varchar(255),
    `allergies` varchar(255),
    `otherIllnesses` varchar(255),
    `idPaciente` int not null,
    primary key (`id`),
    constraint FK_SanitaryPaciente foreign key (`idPaciente`) references pacientes(`id`)
);

create table pharmacy (
    `id` int not null auto_increment,
    `treatment` varchar(255),
    `regularPharmacy` varchar(255),
    `visitFrequency` varchar(100),
    `paymentMethod` varchar(100),
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_PharmacySanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
);

create table nursingMedicine (
    `id` int not null auto_increment,
    `heigth` int,
    `weight` int,
    `nutritionalSituation` varchar(255),
    `sleepQuality` varchar(255),
    `fallRisks` varchar(255),
    `mobilityNeeds` varchar(255),
    `healthPreferences` varchar(255),
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_NursingSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
);

create table socialEducationOccupationalTherapy (
    `id` int not null auto_increment,
    `cognitiveAbilities` varchar(255),
    `affectiveCapacity` varchar(255),
    `behaviorCapacity` varchar(255),
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_SocialEduSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
);

create table socialWork (
    `id` int not null auto_increment,
    `residentAndRelationship` varchar(255),
    `petNameAndBreedPet` varchar(255),
    `collaborationLevel` varchar(255),
    `autonomyLevel` varchar(255),
    `groupParticipation` varchar(255),
    `resources` varchar(255),
    `legalSupport` varchar(255),
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_SocialWorkSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
);

create table kitchenHygiene (
    `id` int not null auto_increment,
    `favouriteFood` varchar(255),
    `dietaryRestrictions` varchar(255),
    `confortAdvices` varchar(255),
    `routine` varchar(255),
    `carePlan` varchar(255),
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_KitchenSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
);

create table otherData (
    `id` int not null auto_increment,
    `photo` varchar(255),
    `professionalNotes` text,
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_OthersSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
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