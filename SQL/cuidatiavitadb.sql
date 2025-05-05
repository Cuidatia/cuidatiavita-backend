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
    `idMaturity` int,
    `idPaciente` int,
	primary key (`id`),
    constraint FK_PacienteLifeStory foreign key (`idPaciente`) references pacientes(`id`)
		on delete cascade
        on update cascade
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
		on delete cascade
        on update cascade
);

create table youth (
    `id` int not null auto_increment,
    `youthStudy` varchar(100),
    `youthSchool` varchar(100),
    `youthWorkplace` varchar(100),
    `youthWorkRole` varchar(100),
    `youthFamilyCore` varchar(100),
    `youthFriendsGroup` varchar(100),
    `youthTravels` varchar(100),
    `youthFavouritePlace` varchar(100),
    `youthRoutine` varchar(100),
    `youthPositiveExperiences` varchar(255),
    `youthNegativeExperiences` varchar(255),
    `youthAddress` varchar(100),
    `youthLikes` varchar(100),
    `youthHobby` varchar(100),
    `youthAfraids` varchar(100),
    `youthProjects` varchar(100),
    `youthUncompletedProjects` varchar(100),
    `youthIllness` varchar(100),
    `youthPersonalCrisis` varchar(100),
    `idLifeStory` int,
    primary key (`id`),
    constraint FK_LifeStoryYouth foreign key (`idLifeStory`) references lifeStory(`id`)
		on delete cascade
        on update cascade
);

create table adulthood (
    `id` int not null auto_increment,
    `sentimentalCoupleAdulthood` varchar(100),
    `childrenAdulthood` varchar(100),
    `adulthoodStudy` varchar(100),
    `adulthoodWorkplace` varchar(100),
    `adulthoodWorkRole` varchar(100),
    `adulthoodFamilyCore` varchar(100),
    `adulthoodFriendsGroup` varchar(100),
    `adulthoodWorkGroup` varchar(100),
    `adulthoodTravels` varchar(100),
    `adulthoodFavouritePlace` varchar(100),
    `adulthoodRoutine` varchar(100),
    `adulthoodPositiveExperiences` varchar(255),
    `adulthoodNegativeExperiences` varchar(255),
    `adulthoodAddress` varchar(100),
    `adulthoodEconomicSituation` varchar(100),
    `adulthoodProjects` varchar(100),
    `adulthoodUncompletedProjects` varchar(100),
    `adulthoodIllness` varchar(100),
    `adulthoodPersonalCrisis` varchar(100),
    `idLifeStory` int,
    primary key (`id`),
    constraint FK_LifeStoryAdulthood foreign key (`idLifeStory`) references lifeStory(`id`)
		on delete cascade
        on update cascade
);

create table maturity (
    `id` int not null auto_increment,
    `grandchildrenMaturity` varchar(100),
    `maturityWorkplace` varchar(100),
    `maturityWorkRole` varchar(100),
    `maturityFamilyCore` varchar(100),
    `maturityFriendsGroup` varchar(100),
    `maturityWorkGroup` varchar(100),
    `maturityTravels` varchar(100),
    `maturityFavouritePlace` varchar(100),
    `maturityRoutine` varchar(100),
    `maturityPositiveExperiences` varchar(255),
    `maturityNegativeExperiences` varchar(255),
    `maturityRetirement` varchar(100),
    `maturityWills` varchar(100),
    `maturityProjects` varchar(100),
    `maturityUncompletedProjects` varchar(100),
    `maturityIllness` varchar(100),
    `maturityPersonalCrisis` varchar(100),
    `idLifeStory` int,
    primary key (`id`),
    constraint FK_LifeStoryMaturity foreign key (`idLifeStory`) references lifeStory(`id`)
		on delete cascade
        on update cascade
);

create table personality (
    `id` int not null auto_increment,
    `nature` varchar(100),
    `habits` varchar(100),
    `likes` varchar(255),
    `dislikes` varchar(255),
    `calmMethods` varchar(100),
    `disturbMethods` varchar(100),
    `hobby` varchar(255),
    `tecnologyLevel` varchar(100),
    `goals` varchar(255),
    `idPaciente` int not null,
    primary key (`id`),
    constraint FK_PacientePersonality foreign key (`idPaciente`) references pacientes(`id`)
		on delete cascade
        on update cascade
);

create table contactData (
    `id` int not null auto_increment,
    `contactName` varchar(100),
    `contactFirstSurname` varchar(100),
    `contactSecondSurname` varchar(100),
    `contactAddress` varchar(100),
    `contactEmail` varchar(100),
    `contactTelecom` varchar(20),
    `idPaciente` int not null,
    primary key (`id`),
    constraint FK_PacienteContact foreign key (`idPaciente`) references pacientes(`id`)
		on delete cascade
        on update cascade
);

create table mainSanitaryData (
    `id` int not null auto_increment,
    `mainIllness` varchar(255),
    `allergies` varchar(255),
    `otherIllnesses` varchar(255),
    `idPaciente` int not null,
    primary key (`id`),
    constraint FK_PacienteSanitary foreign key (`idPaciente`) references pacientes(`id`)
		on delete cascade
        on update cascade
);

create table pharmacy (
    `id` int not null auto_increment,
    `treatment` varchar(255),
    `regularPharmacy` varchar(255),
    `visitFrequency` varchar(100),
    `paymentMethod` enum('S','P','D'),
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_PharmacySanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
);

create table nursingMedicine (
    `id` int not null auto_increment,
    `weight` int,
    `heigth` int,
    `nutritionalSituation` varchar(255),
    `sleepQuality` varchar(255),
    `fallRisks` varchar(255),
    `mobilityNeeds` varchar(255),
    `healthPreferences` varchar(255),
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_NursingSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
);

create table socialEducationOccupationalTherapy (
    `id` int not null auto_increment,
    `cognitiveAbilities` varchar(255),
    `affectiveCapacity` varchar(255),
    `behaviorCapacity` varchar(255),
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_SocialEduSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
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
		on delete cascade
        on update cascade
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
		on delete cascade
        on update cascade
);

create table otherData (
    `id` int not null auto_increment,
    `professionalNotes` text,
    `idSanitary` int not null,
    primary key (`id`),
    constraint FK_OthersSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
);

create table images(
    `id` int not null auto_increment,
    `photoReferences` varchar(255) not null,
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