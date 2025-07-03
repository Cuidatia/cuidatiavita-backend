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
    `description` varchar(255) null,
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
    `idOrganizacion` int not null,
    `name` varchar(100) not null,
    `firstSurname` varchar(100) not null,
    `secondSurname` varchar(100) not null,
    `alias` varchar(50) not null,
    `birthDate` date not null,
    `age` int not null,
    `birthPlace` varchar(100),
    `nationality` varchar(50) not null,
    `gender` enum('M','F','O') not null,
    `address` varchar(100) not null,
    `maritalStatus` enum('ST','C', 'V', 'S', 'D', 'P') not null,
    `sentimentalCouple` varchar(100),
    `language` varchar(20) not null,
    `otherLanguages` varchar(50),
    `culturalHeritage` varchar(255),
    `faith` varchar(100),
    `time_added_paciente` TIMESTAMP DEFAULT current_timestamp,
    primary key (`id`),
    constraint FK_PacienteOrganizacion foreign key (`idOrganizacion`) references organizaciones(`id`)
		on delete cascade
        on update cascade
);

create table lifeStory(
	`id` int not null auto_increment,
    `idPaciente` int not null,
	primary key (`id`),
    constraint FK_PacienteLifeStory foreign key (`idPaciente`) references pacientes(`id`)
		on delete cascade
        on update cascade
);

create table childhood(
    `id` int not null auto_increment,
    `idLifeStory` int not null,
    `childhoodStudies` varchar(100),
    `childhoodSchool` varchar(100),
    `childhoodMotivations`varchar(100),
    `childhoodFamilyCore` varchar(100),
    `childhoodFriendsGroup` varchar(100),
    `childhoodImportantPerson` varchar(100),
    `childhoodTravels` varchar(100),
    `childhoodFavouritePlace` varchar(100),
    `childhoodPositiveExperiences` varchar(255),
    `childhoodNegativeExperiences` varchar(255),
    `childhoodResponsabilities` varchar(100),
    `childhoodAddress` varchar(100),
    `childhoodLikes` varchar(100),
    `childhoodAfraids` varchar(100),
    primary key (`id`),
    constraint FK_LifeStoryChilhood foreign key (`idLifestory`) references lifeStory(`id`)
		on delete cascade
        on update cascade
);

create table youth (
    `id` int not null auto_increment,
    `idLifeStory` int not null,
    `youthStudies` varchar(100),
    `youthSchool` varchar(100),
    `youthWorkPlace` varchar(100),
    `youthWorkRol` varchar(100),
    `youthFamilyCore` varchar(100),
    `youthFriendsGroup` varchar(100),
    `youthImportantPerson` varchar(100),
    `youthTravels` varchar(100),
    `youthFavouritePlace` varchar(100),
    `youthRoutine` varchar(100),
    `youthPositiveExperiences` varchar(255),
    `youthNegativeExperiences` varchar(255),
    `youthResponsabilities` varchar(100),
    `youthAddress` varchar(100),
    `youthLikes` varchar(100),
    `youthHobbies` varchar(100),
    `youthAfraids` varchar(100),
    `youthSentimentalCouple` varchar(255),
    `youthProjects` varchar(100),
    `youthUncompletedProjects` varchar(100),
    `youthIllness` varchar(100),
    `youthPersonalCrisis` varchar(100),

    primary key (`id`),
    constraint FK_LifeStoryYouth foreign key (`idLifeStory`) references lifeStory(`id`)
		on delete cascade
        on update cascade
);

create table adulthood (
    `id` int not null auto_increment,
    `idLifeStory` int not null,
    `adulthoodSentimentalCouple` varchar(100),
    `adulthoodChildren` varchar(100),
    `adulthoodStudies` varchar(100),
    `adulthoodWorkPlace` varchar(100),
    `adulthoodWorkRol` varchar(100),
    `adulthoodFamilyCore` varchar(100),
    `adulthoodFriendsGroup` varchar(100),
    `adulthoodWorkGroup` varchar(100),
    `adulthoodImportantPerson` varchar(100),
    `adulthoodTravels` varchar(100),
    `adulthoodFavouritePlace` varchar(100),
    `adulthoodRoutine` varchar(100),
    `adulthoodPositiveExperiences` varchar(255),
    `adulthoodNegativeExperiences` varchar(255),
    `adulthoodResponsabilities` varchar(100),
    `adulthoodAddress` varchar(100),
    `adulthoodEconomicSituation` varchar(100),
    `adulthoodProjects` varchar(100),
    `adulthoodUncompletedProjects` varchar(100),
    `adulthoodIllness` varchar(100),
    `adulthoodPersonalCrisis` varchar(100),
    primary key (`id`),
    constraint FK_LifeStoryAdulthood foreign key (`idLifeStory`) references lifeStory(`id`)
		on delete cascade
        on update cascade
);

create table maturity (
    `id` int not null auto_increment,
    `idLifeStory` int not null,
    `maturityGrandchildren` varchar(100),
    `maturityWorkPlace` varchar(100),
    `maturityWorkRol` varchar(100),
    `maturityFamilyCore` varchar(100),
    `maturityFriendsGroup` varchar(100),
    `maturityWorkGroup` varchar(100),
    `maturityImportantPerson` varchar(100),
    `maturityTravels` varchar(100),
    `maturityFavouritePlace` varchar(100),
    `maturityRoutine` varchar(100),
    `maturityPositiveExperiences` varchar(255),
    `maturityNegativeExperiences` varchar(255),
    `maturityResponsabilities` varchar(100),
    `maturityRetirement` varchar(100),
    `maturityWills` varchar(100),
    `maturityProjects` varchar(100),
    `maturityUncompletedProjects` varchar(100),
    `maturityIllness` varchar(100),
    `maturityPersonalCrisis` varchar(100),
    primary key (`id`),
    constraint FK_LifeStoryMaturity foreign key (`idLifeStory`) references lifeStory(`id`)
		on delete cascade
        on update cascade
);

create table personality (
    `id` int not null auto_increment,
    `idPaciente` int not null,
    `nature` varchar(100),
    `habits` varchar(100),
    `likes` varchar(255),
    `dislikes` varchar(255),
    `calmMethods` varchar(100),
    `disturbMethods` varchar(100),
    `hobbies` varchar(255),
    `technologyLevel` varchar(100),
    `goals` varchar(255),
    `favouriteSongs` varchar(255),
    `clothes` varchar(255),
    primary key (`id`),
    constraint FK_PacientePersonality foreign key (`idPaciente`) references pacientes(`id`)
		on delete cascade
        on update cascade
);

create table contactData (
    `id` int not null auto_increment,
    `idPaciente` int not null,
    `contactName` varchar(100),
    `contactFirstSurname` varchar(100),
    `contactSecondSurname` varchar(100),
    `contactAddress` varchar(100),
    `contactEmail` varchar(100),
    `contactTelecom` varchar(20),
    `curatela` varchar(100),
    `deFactoGuardian` varchar(100),
    primary key (`id`),
    constraint FK_PacienteContact foreign key (`idPaciente`) references pacientes(`id`)
		on delete cascade
        on update cascade
);

create table mainSanitaryData (
    `id` int not null auto_increment,
    `idPaciente` int not null,
    `mainIllness` varchar(255),
    `allergies` varchar(255),
    `otherIllness` varchar(255),
    primary key (`id`),
    constraint FK_PacienteSanitary foreign key (`idPaciente`) references pacientes(`id`)
		on delete cascade
        on update cascade
);

create table pharmacy (
    `id` int not null auto_increment,
    `idSanitary` int not null,
    `treatment` varchar(255),
    `regularPharmacy` varchar(255),
    `visitFrequency` varchar(100),
    `paymentMethod` enum('S','P','D'),
    primary key (`id`),
    constraint FK_PharmacySanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
);

create table nursingMedicine (
    `id` int not null auto_increment,
    `idSanitary` int not null,
    `nutritionalSituation` varchar(255),
    `sleepQuality` varchar(255),
    `fallRisks` varchar(255),
    `mobilityNeeds` varchar(255),
    `healthPreferences` varchar(255),
    primary key (`id`),
    constraint FK_NursingSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
);

create table socialEducationOccupationalTherapy (
    `id` int not null auto_increment,
    `idSanitary` int not null,
    `cognitiveAbilities` varchar(255),
    `affectiveCapacity` varchar(255),
    `behaviorCapacity` varchar(255),
    `collaborationLevel` varchar(255),
    `autonomyLevel` varchar(255),
    `groupParticipation` varchar(255),
    primary key (`id`),
    constraint FK_SocialEduSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
);

create table socialWork (
    `id` int not null auto_increment,
    `idSanitary` int not null,
    `residentAndRelationship` varchar(255),
    `petNameAndBreedPet` varchar(255),
    `resources` varchar(255),
    `legalSupport` varchar(255),
    primary key (`id`),
    constraint FK_SocialWorkSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
);

create table kitchenHygiene (
    `id` int not null auto_increment,
    `idSanitary` int not null,
    `favouriteFood` varchar(255),
    `dietaryRestrictions` varchar(255),
    `confortAdvices` varchar(255),
    `routine` varchar(255),
    `carePlan` varchar(255),
    primary key (`id`),
    constraint FK_KitchenSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
);

create table otherData (
    `id` int not null auto_increment,
    `idSanitary` int not null,
    `professionalNotes` text,
    primary key (`id`),
    constraint FK_OthersSanitary foreign key (`idSanitary`) references mainSanitaryData(`id`)
		on delete cascade
        on update cascade
);

create table images(
    `id` int not null auto_increment,
    `idPaciente` int not null,
    `photoReferences` varchar(255) not null,
    `photoCategory` enum('P','I', 'J', 'A', 'M', 'G') not null,
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
insert into usuarios (nombre, email, password, idOrganizacion) values ('Juan Alberto Torró Gómez', 'user1@prueba.es','123456',2);
insert into usuarios (nombre, email, password, idOrganizacion) values ('Paula Guilbert Arnau', 'user2@prueba.es','123456',2);
insert into usuarios (nombre, email, password, idOrganizacion) values ('Dejan Ishult Trigueros', 'user3@prueba.es','123456',2);
insert into usuarios (nombre, email, password, idOrganizacion) values ('Jaime Lima Mata', 'user4@prueba.es','123456',2);
insert into usuarios (nombre, email, password, idOrganizacion) values ('Elena Nito Del Bosque', 'user5@prueba.es','123456',2);

insert into roles (`nombre`) values ('superadmin');
insert into roles (`nombre`, `description`) values ('administrador', 'Administrador de la organización; Visualiza todos los datos de la organización;  Añade, modifica y elimina usuarios de la organización; Añade, modifica y elimina pacientes de la organización; Accede a todos los datos de los pacientes de la organización;');
insert into roles (`nombre`, `description`) values ('medico/enfermero', 'Personal sanitario; Añade, modifica y elimina pacientes de la organización; Añade, modifica y elimina los datos generales y los datos sanitarios correspondientes a las sección Medicina/Efermería de los pacientes de la organización;');
insert into roles (`nombre`, `description`) values ('trabajador social', 'Añade, modifica y elimina pacientes de la organización; Añade, modifica y elimina los datos generales y los datos sanitarios correspondientes a las sección Trabajo Social de los pacientes de la organización;');
insert into roles (`nombre`, `description`) values ('educador social/terapeuta ocupacional', 'Añade, modifica y elimina pacientes de la organización; Añade, modifica y elimina los datos generales y los datos sanitarios correspondientes a las sección Educación Social/Terapia Ocupacional de los pacientes de la organización;');
insert into roles (`nombre`, `description`) values ('auxiliar', 'Visualiza los datos generales y los datos sanitarios correspondientes a las sección Cocina/Higiene de los pacientes de la organización;');
insert into roles (`nombre`, `description`) values ('profesional de referencia', 'Acceso diecto a los pacientes de la organización que le han sido asignados');
insert into roles (`nombre`, `description`) values ('familiar', 'Acceso diecto a los pacientes de la organización que le han sido asignados como familiar');

insert into usuario_roles (`idUsuario`, `idRol`) values (1, 1); 
insert into usuario_roles (`idUsuario`, `idRol`) values (2, 2);
insert into usuario_roles (`idUsuario`, `idRol`) values (3, 3);
insert into usuario_roles (`idUsuario`, `idRol`) values (4, 4);
insert into usuario_roles (`idUsuario`, `idRol`) values (5, 5);
insert into usuario_roles (`idUsuario`, `idRol`) values (6, 6);
insert into usuario_roles (`idUsuario`, `idRol`) values (7, 6);

INSERT INTO pacientes (idOrganizacion, name, firstSurname, secondSurname, alias, birthDate, age, birthPlace,nationality, gender, address, maritalStatus, sentimentalCouple,language, otherLanguages, culturalHeritage, faith) VALUES (
    2, 'Carlos', 'Martínez', 'Ruiz', 'Prueba', '1955-07-12', 70, 'Madrid','Española', 'M', 'Calle Mayor 45, Madrid', 'C','', 'Español', 'Inglés, Francés','Mediterránea', 'Católica'
);
INSERT INTO lifeStory (idPaciente) VALUES (1);
INSERT INTO childhood (idLifeStory, childhoodStudies, childhoodSchool, childhoodMotivations, childhoodFamilyCore,childhoodFriendsGroup, childhoodImportantPerson,childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,childhoodNegativeExperiences,childhoodResponsabilities, childhoodAddress, childhoodLikes, childhoodAfraids) VALUES (
    1, 'Primaria completa', 'Colegio San Juan', 'Aprender y jugar','Padres y una hermana', 'Grupo del barrio','', 'Viajes a la playa', 'Parque del Retiro','Excursiones familiares', 'Separación de sus padres', '','Calle Toledo 33', 'Bicicletas y animales', 'Oscuridad');
INSERT INTO youth (
    idLifeStory, youthStudies, youthSchool, youthWorkPlace, youthWorkRol, youthFamilyCore,youthFriendsGroup, youthImportantPerson, youthTravels, youthFavouritePlace, youthRoutine, youthPositiveExperiences,
    youthNegativeExperiences,youthResponsabilities, youthAddress, youthLikes, youthHobbies, youthAfraids, youthSentimentalCouple,youthProjects, youthUncompletedProjects, youthIllness, youthPersonalCrisis) VALUES (
    1, 'Bachillerato técnico', 'IES Cervantes', 'Tienda de informática', 'Ayudante técnico','Madre y hermana', 'Amigos del instituto', '','Intercambio en Francia', 'Sala de ordenadores',
    'Estudiar y trabajar', 'Primer concierto', 'Rechazo social', '','Calle Pez 12','Tecnología', 'Videojuegos y música', 'Fracaso', '','Estudiar ingeniería', 'Viajar al extranjero','Gripe fuerte', 'Fallecimiento del abuelo');
INSERT INTO adulthood (
    idLifeStory, adulthoodSentimentalCouple, adulthoodChildren, adulthoodStudies,adulthoodWorkPlace, adulthoodWorkRol, adulthoodFamilyCore, adulthoodFriendsGroup,adulthoodWorkGroup, adulthoodImportantPerson,adulthoodTravels, adulthoodFavouritePlace, adulthoodRoutine,
    adulthoodPositiveExperiences, adulthoodNegativeExperiences, adulthoodResponsabilities, adulthoodAddress,adulthoodEconomicSituation, adulthoodProjects, adulthoodUncompletedProjects,adulthoodIllness, adulthoodPersonalCrisis) VALUES (
    1,'Laura Gómez', '2 hijos', 'Grado en informática','Empresa TecSoluciones', 'Desarrollador Backend', 'Pareja e hijos','Grupo de padres del colegio', 'Equipo de desarrollo','', 'Italia, Japón',
    'Casa rural en Segovia', 'Trabajo y familia', 'Nacimiento del primer hijo','Desempleo durante 1 año', '','Av. de América 22', 'Estable','Crear app educativa', 'Montar empresa propia', 'Alergia al polen','Divorcio complicado');
INSERT INTO maturity (
    idLifeStory, maturityGrandchildren, maturityWorkPlace, maturityWorkRol, maturityFamilyCore,maturityFriendsGroup, maturityWorkGroup, maturityImportantPerson,maturityTravels, maturityFavouritePlace,
    maturityRoutine, maturityPositiveExperiences, maturityNegativeExperiences,maturityResponsabilities, maturityRetirement,maturityWills, maturityProjects, maturityUncompletedProjects, maturityIllness, maturityPersonalCrisis) VALUES (
    1, '3 nietos', 'Universidad Complutense', 'Profesor asociado', 'Hijos y nietos','Amigos del barrio', 'Departamento de TIC','', 'Portugal, Grecia','Chalet en la sierra', 'Lectura y paseos', 'Graduación de los nietos',
    'Pérdida de amigos', '','A los 65 años', 'Dejar legado educativo','Escribir un libro', 'Viaje a Asia', 'Hipertensión','Aislamiento emocional tras jubilación');
INSERT INTO personality (
    idPaciente, nature, habits, likes, dislikes, calmMethods, disturbMethods, hobbies, technologyLevel, goals, favouriteSongs, clothes) VALUES (
    1, 'Tranquilo y reflexivo', 'Caminar diario, leer antes de dormir','Música clásica, comida mediterránea', 'Ruido, multitudes', 'Meditación, lectura',
    'Caos, desorganización', 'Escritura, jardinería','Alto, usa tecnología a diario', 'Inspirar a sus nietos','Clair de Lune, Bohemian Rhapsody', 'Informal elegante, colores neutros');
INSERT INTO contactData (idPaciente, contactName, contactFirstSurname, contactSecondSurname,contactAddress, contactEmail, contactTelecom, curatela, deFactoGuardian) VALUES (
    1, 'Laura', 'Gómez', 'Navarro', 'Calle Alcalá 123, Madrid','laura_gomez@example.com', '612345678', 'Ninguna', 'Hija mayor');
INSERT INTO mainSanitaryData (idPaciente, mainIllness, allergies, otherIllness) VALUES (
    1, 'Hipertensión', 'Alergia al polvo', 'Dolor lumbar crónico');
INSERT INTO pharmacy (idSanitary, treatment, regularPharmacy, visitFrequency, paymentMethod) VALUES (
    1, 'Enalapril 10mg diario', 'Farmacia del Carmen', 'Mensual', 'S');
INSERT INTO nursingMedicine (idSanitary, nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences) VALUES (
    1, 'Dieta equilibrada', 'Sueño ligero pero suficiente', 'Bajo riesgo', 'Camina con bastón', 'Prefiere tratamientos naturales');
INSERT INTO socialEducationOccupationalTherapy (idSanitary, cognitiveAbilities, affectiveCapacity, behaviorCapacity,collaborationLevel, autonomyLevel, groupParticipation) VALUES (
    1, 'Ligeramente reducidas', 'Estable', 'Cooperativo','Alto', 'Autónomo con supervisión', 'Activa en actividades grupales');
INSERT INTO socialWork (idSanitary, residentAndRelationship, petNameAndBreedPet, resources, legalSupport) VALUES (
    1, 'Vive con su hijo menor', 'Luna - Labrador', 'Pensión y ayuda social','Asistencia legal comunitaria');
INSERT INTO kitchenHygiene (idSanitary, favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan) VALUES (
    1, 'Paella', 'Reducir sal', 'Cocina con ventilación y buena iluminación', 'Cocina una vez al día', 'Supervisión semanal por nutricionista');
INSERT INTO otherData (idSanitary, professionalNotes) VALUES (
    1, 'Paciente colaborador, con buena disposición para programas de integración social. Se recomienda seguimiento psicológico preventivo anual.');

INSERT INTO pacientes (
    idOrganizacion, name, firstSurname, secondSurname, alias, birthDate, age, birthPlace,
    nationality, gender, address, maritalStatus, sentimentalCouple,language, otherLanguages, culturalHeritage, faith
) VALUES (
    2, 'Jacinto', 'Llopis', 'Hierro', 'Prueba', 
    '1945-02-25', 80, 'Valencia', 'Española', 'M', 
    'Calle de Amor Bueno 93, Navarra, 86379', 'C','', 'Español', 'Italiano, Abjasio', 
    'Valenciano', 'Cristiano'
);

INSERT INTO pacientes (
    idOrganizacion, name, firstSurname, secondSurname, alias, birthDate, age, birthPlace,
    nationality, gender, address, maritalStatus, sentimentalCouple,language, otherLanguages, culturalHeritage, faith
) VALUES (
    2, 'Noelia', 'Lobo', 'Cortés', 'Prueba', 
    '1947-07-09', 78, 'Badajoz', 'Española', 'F', 
    'Acceso Rebeca Núñez 840 Puerta 1 , Ávila, 95931', 'V','', 'Español', 'Ninguno', 
    'Castellana', 'Crsitiana'
);

INSERT INTO pacientes (
    idOrganizacion, name, firstSurname, secondSurname, alias, birthDate, age, birthPlace,
    nationality, gender, address, maritalStatus, sentimentalCouple,language, otherLanguages, culturalHeritage, faith
) VALUES (
    2, 'Rita', 'Guerrero', 'Cabrero', 'Prueba', 
    '1940-11-10', 84, 'Lleida', 'Española', 'F', 
    'Acceso de Hugo Lasa 3, Cáceres, 64835', 'C', '','Español', 'Inglés, Catalán, Francés', 
    'Catalana', 'Atea'
);

INSERT INTO pacientes (
    idOrganizacion, name, firstSurname, secondSurname, alias, birthDate, age, birthPlace,
    nationality, gender, address, maritalStatus,sentimentalCouple, language, otherLanguages, culturalHeritage, faith
) VALUES (
    2, 'Julio', 'Batalla', 'Galván', 'Prueba', 
    '1954-08-07', 71, 'Castellón', 'Española', 'M', 
    'Vial de Juan Manuel Chaparro 98 Piso 9 , Palencia, 53287', 'C','', 'Español', 'Inglés, Catalán', 
    'Valenciano', 'Cristiano'
);

INSERT INTO pacientes (
    idOrganizacion, name, firstSurname, secondSurname, alias, birthDate, age, birthPlace,
    nationality, gender, address, maritalStatus,sentimentalCouple, language, otherLanguages, culturalHeritage, faith
) VALUES (
    2, 'Mónica', 'Roca', 'Bartolomé', 'Prueba', 
    '1951-10-10', 73, 'Pontevedra', 'Española', 'F', 
    'Via Isabel Lasa 51 Piso 2 , Álava, 82814', 'C','', 'Español', 'Ninguno', 
    'Gallega', 'Cristiana'
);

INSERT INTO pacientes (
    idOrganizacion, name, firstSurname, secondSurname, alias, birthDate, age, birthPlace,
    nationality, gender, address, maritalStatus, sentimentalCouple,language, otherLanguages, culturalHeritage, faith
) VALUES (
    2, 'Raúl', 'Cuéllar', 'Barco', 'Prueba', 
    '1950-10-20', 74, 'Madrid', 'Española', 'M', 
    'Cañada de Jose Barco 29, Toledo, 18227', 'C','', 'Español', 'Inglés, Portugués, Francés', 
    'Castellano', 'Cristiano'
);

INSERT INTO lifeStory (idPaciente) VALUES (2);
INSERT INTO lifeStory (idPaciente) VALUES (3);
INSERT INTO lifeStory (idPaciente) VALUES (4);
INSERT INTO lifeStory (idPaciente) VALUES (5);
INSERT INTO lifeStory (idPaciente) VALUES (6);
INSERT INTO lifeStory (idPaciente) VALUES (7);

INSERT INTO childhood (
    idLifeStory, childhoodStudies, childhoodSchool, childhoodMotivations, childhoodFamilyCore,
    childhoodFriendsGroup, childhoodImportantPerson,childhoodTravels, childhoodFavouritePlace, childhoodPositiveExperiences,
    childhoodNegativeExperiences, childhoodResponsabilities, childhoodAddress, childhoodLikes, childhoodAfraids
) VALUES
(2, 'Primaria completa',         'Colegio San Vicente',  'Jugar con amigos',         'Familia numerosa (4 hermanos)',   'Amigos del barrio',  '',     'Veranos en la playa',   'Patio de la escuela',      'Excursión al zoológico',      'Enfermedad de un hermano',  '',    'C/ Olivo 12, Sevilla',    'Dibujar y fútbol',        'Tormentas'),
(3, 'Primaria completa',       'Colegio Nuestra Señora', 'Leer libros de aventuras', 'Vive con madre y abuelos',        'Vecinos de la finca',   '',  'Visitas a Granada',      'Parque del pueblo',        'Fiesta de cumpleaños cada año', 'Pérdida del abuelo',        '',    'Av. Los Pinos 5, Bilbao','Coleccionar sellos',     'Alturas'),
(4, 'Primaria completa',         'Escuela Pública Nº3',    'Explorar la naturaleza',    'Padres separados',                'Primos y vecinos',   '',    'Excursiones familiares', 'Río cercano',             'Primer campamento escolar',     'Bullying en el cole',        '',   'C/ Luna 23, Zaragoza',   'Insectos y armar puzzles', 'Ruido fuerte'),
(5, 'Primaria completa',         'Colegio Santa María',    'Aprender a leer',           'Vive en un orfanato',                'Niños del orfanato', '',    'Viaje a Barcelona',      'Biblioteca local',        'Concurso de dibujo',            'Cambio de colegio repetido',  '',  'Pº Sta. Catalina 8, Murcia','Cantar y pintar',      'Perderse solo'),
(6, 'Primaria completa',       'Colegio Montesol',       'Ver películas de ciencia',  'Familia extendida grande',        'Amigos del vecindario', '', 'Visitas a la montaña',   'Huerto familiar',         'Fiesta patronal anual',          'Accidente leve en bici',    '',    'C/ San Roque 19, Málaga','Ciencia y animales',      'Oscuridad'),
(7, 'Primaria completa',         'Colegio Cristo Rey',     'Hacer teatro escolar',      'Hijo único',                      'Compañeros de clases', '',  'Viaje a Portugal',       'Auditorio municipal',     'Obra de teatro en familia',     'Divorcio de los padres',   '',      'C/ Naranjo 47, Valladolid','Cantar y bailar',       'Perder juguetes');

INSERT INTO youth (
    idLifeStory, youthStudies, youthSchool, youthWorkPlace, youthWorkRol, youthFamilyCore,
    youthFriendsGroup,youthImportantPerson, youthTravels, youthFavouritePlace, youthRoutine, youthPositiveExperiences,
    youthNegativeExperiences, youthResponsabilities, youthAddress, youthLikes, youthHobbies, youthAfraids, youthSentimentalCouple,
    youthProjects, youthUncompletedProjects, youthIllness, youthPersonalCrisis
) VALUES
(2, 'ESO completa',       'IES El Terruño',     'Cafetería Estrella',   'Camarero',      'Madre y 4 hermanos',         'Amigos del instituto', '',    'Intercambio Erasmus (Portugal)', 'Sala de estudio',     'Estudiar y trabajo parcial',   'Primeros exámenes aprobados',       'Ruptura con noviazgo',       '',    'C/ Olivo 12, Sevilla',   'Música rock',           'Fútbol', '','', 'Crear banda musical', 'No finalizar bachillerato', 'Apendicitis','Alcoholismo familiar'),
(3, 'ESO incompleta',     'IES Bilbao Centro',  'Tienda de ropa',      'Dependiente',  'Padre viudo, vive con abuela',    'Vecinos y primos',  '',        'Viaje de fin de curso a París', 'Centro juvenil',      'Clases y trabajo de fin de semana','Tercer puesto en campeonato  de futsal', 'Muerte de la madre',         '',    'Av. Los Pinos 5, Bilbao','Videos de YouTube', 'Baloncesto', '','', 'Montar un taller mecánico','',    'Gripe grave', ''),
(4, 'ESO completa',       'IES Pilar Lorengar', 'Fábrica de plásticos', 'Operario',     'Padres separados, vive con padre', 'Amigos de clase',  '',         'No viajó a ningún sitio',        'Cafetería del barrio',  'Trabajo por turnos',            'Aprender primeros auxilios',       'Problemas de adaptación social', '',   'C/ Luna 23, Zaragoza',   'Música electrónica', 'Videojuegos', '', '','', 'Sin lograrlo por falta de recursos','No sufrió ninguna enfermedad', ''),
(5, 'Bachillerato artístico', 'IES La Marina', 'Restaurante La Brisa', 'Ayudante de cocina','Vive en orfanato hasta 18 años', 'Compañeros del orfanato',  '',  'Verano en Cuba',             'Estudio de arte',       'Prácticas de cocina',            'Primer premio de pintura',          '',  '',  'Pº Sta. Catalina 8, Murcia','Arte contemporáneo',    'Pintura y dibujo','Rendirse ante el estrés', '','Exponer sus obras en una galería local',  'No culminar bachillerato', 'No sufrió ninguna enfermedad', 'Ansiedad'),
(6, 'ESO completa',       'IES Montesol',       'Visitas a residencia ancianos','Voluntariado',  'Familia extensa unida',       'Amigos de barrio','',       'Viaje a Francia con familia', 'Biblioteca municipal',  'Equilibrar estudios y voluntariado','Premio local de escritura',     '',     '',    'C/ San Roque 19, Málaga','Lectura de poesía', 'Cuentacuentos', 'Sufrir rechazo social', '','Publicar un cuento infantil', '', '',  ''),
(7, 'Bachillerato científico','IES Buenavista','Laboratorio Unitech',  'Practicante de laboratorio','Hijo único','Círculo de estudio', '',     'No ha viajado', 'Biblioteca universitaria','Estudiar y hacer voluntariado', 'Publicar artículo en revista',    'Fracaso en oposición',    '',           'C/ Naranjo 47, Valladolid','Astronomía', 'Ajedrez', '','', '',   'No terminar grado universitario','Neumonía', 'Estrés universitario');

INSERT INTO adulthood (
    idLifeStory, adulthoodSentimentalCouple, adulthoodChildren, adulthoodStudies,
    adulthoodWorkPlace, adulthoodWorkRol, adulthoodFamilyCore, adulthoodFriendsGroup,
    adulthoodWorkGroup, adulthoodImportantPerson,adulthoodTravels, adulthoodFavouritePlace, adulthoodRoutine,
    adulthoodPositiveExperiences, adulthoodNegativeExperiences, adulthoodResponsabilities, adulthoodAddress,
    adulthoodEconomicSituation, adulthoodProjects, adulthoodUncompletedProjects,
    adulthoodIllness, adulthoodPersonalCrisis
) VALUES
(2, 'Ana Ruiz', 'Solo tuvo un hijo, Óscar', 'Grado en Educación', 'Colegio El Olivar', 'Profesor de primaria', 'Su mujer y su hijo', 'Profesorado y padres', 'Equipo docente','', 'Italia y Marruecos', 'Casa familiar', 'Clases y vida familiar', 'Estudiar para las oposiciones', 'Crisis laboral en 2009','', 'C/ Olivo 12, Sevilla', 'Estable', '', '', 'Migraña crónica', ''),
(3, 'Miguel Ortega', '2 hijas', 'Grado en Comercio', 'Supermercado Central', 'Jefa de sección', 'Su marido y sus hijas', 'Familia cercana', 'Equipo de ventas','', 'Francia', 'La cafetería de su amiga', 'Trabajo y compras', 'Ascenso a directora de zona', 'Problemas económicos en 2013', '', 'Plaza Los Pinos 5, Bilbao','Ajustada', 'Montar su tienda propia', '', 'Tensión arterial alta', 'No padece ningún problema'),
(4, 'Carlos Pérez', 'Su hija Eva', 'Ingeniería Química',  'Refinería Río Ebro', 'Ingeniera de procesos','Pareja e hija', 'Compañeros de la facultad', 'Compañeros de la planta de producción','', 'Suecia y Alemania',  '',  'Suele realizar viajes a menudo, ayudando a su familia', 'Ascender dentro de la empresa', '', '','C/ Luna 23, Zaragoza', 'Bueno', 'Investigar biocombustibles', 'Proyecto detenido por falta de inversión','Asma', 'Estrés por presión laboral'),
(5, 'Laura Díaz',    'Sus hijos Pilar y David', 'Bellas Artes', 'Galería de arte local', 'Pintora', 'Su marido, su madre y sus hijos', 'Los artistas de la ciudad','Artistas locales','', 'Viajó a Nueva York', 'La galería de arte en la que trabaja', 'Está toda la mañana en la galería de artes y luego pasa tiempo con la familia', 'Exposición en museo internacional', 'Crisis creativa en 2015', '', 'Pº Sta. Catalina 8, Murcia','Ajustada', 'Fundar su escuela de arte', 'No tiene nada que remarcar',  'No sufrió ninguna enfermedad remarcable', 'Insatisfacción personal'),
(6, 'Borja Díaz',     'No tuvieron hijos', 'Filología Hispánica', 'Editorial Acacia','Correctora de estilo', 'Su pareja',  'Los amigos de su pareja y sus hijos jóvenes', 'Club de lectura','', 'Solo viajó por España','', 'Trabajo remoto y familia', 'Publicar un libro propio', 'Baja de la editorial en 2020', '', 'C/ San Roque 19, Málaga', 'Estable','', 'Organizar un taller literario', '', 'Bloqueo creativo'),
(7, 'Sara López',       'Tuvo una hija llamada Victoria', 'Biología', 'Hospital Universitario', 'Investigador',  'Su pareja y su hija', 'Los científicos del laboratorio', 'Red de científicos','', 'Viajó por España',  '', '', 'Publicar artículo en Nature', 'Financiación denegada 2019', '', 'C/ Naranjo 47, Valladolid', 'Buena', '',  '', '', '');

INSERT INTO maturity (
    idLifeStory, maturityGrandchildren, maturityWorkPlace, maturityWorkRol, maturityFamilyCore,
    maturityFriendsGroup, maturityWorkGroup, maturityImportantPerson,maturityTravels, maturityFavouritePlace,
    maturityRoutine, maturityPositiveExperiences, maturityNegativeExperiences, maturityResponsabilities, maturityRetirement,
    maturityWills, maturityProjects, maturityUncompletedProjects, maturityIllness, maturityPersonalCrisis
) VALUES
(2, '2 nietos',        'Escuela Infantil La Paz', 'Director',        'Hijos, nietos y esposa', 'Colegas de educación',   'Equipo directivo','',          'Portugal y Marruecos',    'Casa rural en Sierra Morena', 'Visitas al centro de día',  'Poder conocer a su bisnieto',      'Pérdida de amigos de la infancia',     '', 'A los 65 años',    'Dejar becas para los niños',   '',     '',     '',''),
(3, 'Sin nietos',      'Clínica San José',        'Administrativa',  'Hijas y madre anciana',     'Vecinas de comunidad',    'Equipo de administración', '','Grecia y Turquía',        'Apartamento en la playa',        'Lectura matutina',         'Recuperación de una operación grande',  'Aislamiento social progresivo',      '', 'A los 60 años',    'Quiere escribir sus memorias',       '',     '',     '',''),
(4, '1 nieto',         'Refinería Río Ebro',       'Consultora',       'Esposa e hijo adulto',      'Amigos de facultad',      'Equipo de I+D',       '',    'Suecia y Alemania',       'Finca en el campo',            'Jardinería diaria',        'Proyecto de biocombustibles finalizado', 'Accidentes automovilísticos leves', '', 'A los 62 años',    '','',     '',     '',''),
(5, '2 nietos',        'Museo de Bellas Artes',    'Director adjunto', 'Hija y nietos',            'Artistas locales senior', 'Equipo curatorial',   '',    'Nueva York y París',      'Chalet con estudio de arte',    'Pintar cada mañana',       'Tener exposición retrospectiva',         'Crisis económica global 2020',        '', 'A los 65 años',    'Crear fundación de arte',  '',     '',     '',''),
(6, 'Sin nietos',      'Editorial Acacia',         'Editora jefa',    'Pareja',       'Club literario',          'Departamento editorial', '', 'Reino Unido y Argentina', 'Casa en Málaga',               'Escritura diaria',        'Publicar su primera novela',          'Problemas de visión por años de lectura', '', 'A los 65 años',    '',   '',     '',     '',''),
(7, '1 nieto',         'Hospital Universitario',   'Investigador principal','Hija y nieto' ,          'Red de científicos','Equipo de investigación','','Japón y EE.UU.',          'Vivienda en Valladolid',         'Pasar tiempo en el laboratorio y luego ver a su nieto',      'Publicar artículo de alto impacto',     'Pérdida de colegas por jubilación',   '',  'A los 63 años',    'Donar equipo de laboratorio', '',     '',     '','');

INSERT INTO personality (
    idPaciente, nature, habits, likes, dislikes, calmMethods, disturbMethods,
    hobbies, technologyLevel, goals, favouriteSongs, clothes
) VALUES
(2, 'Extrovertido y cariñoso', 'Correr cada mañana, escribir diario',
    'Niños, música infantil', 'Soledad', 'Yoga y caminatas', 'Silencio absoluto',
    'Pintar y jardinería', 'Básico (solo redes sociales)', 'Educar a su hijo con valores',
    'La cucaracha, We are the champions', 'Ropa cómoda y colorida'
),
(3, 'Reservada y analítica', 'Leer cada noche, hacer puzzles',
    'Animales, pintar', 'Multitudes ruidosas', 'Música clásica suave', 'Discursos largos',
    'Coleccionar figuritas', 'Intermedio (internet y correo)', 'Vender su propia tienda',
    'No me platiques más, Ave María', 'Vestidos y tonos pastel'
),
(4, 'Pragmático y metódico', 'Ordenar su taller, hacer deporte',
    'Café, bricolaje', 'Desorden', 'Técnicas de respiración', 'Caos en el taller',
    'Mecánica y senderismo', 'Alto (proyectos de I+D)', 'Desarrollar producto sostenible',
    'Time, Imagine', 'Ropa de trabajo funcional'
),
(5, 'Creativo y soñador', 'Esbozar ideas, escuchar música', 
    'Museos, charlas artísticas', 'Rutina excesiva', 'Arte y meditación', 'Críticas negativas',
    'Dibujo, escultura', 'Bajo (solo redes sociales)', 'Tener galería propia',
    'Blue Monday, Yellow Submarine', 'Prendas bohemias y coloridas'
),
(6, 'Soñadora y empática', 'Leer poesía, caminar descalza',
    'Café con amigas, libros', 'Ruido urbano', 'Terapia artística', 'Críticas destructivas',
    'Escritura creativa, yoga', 'Medio (uso diario de PC)', 'Publicar novela bestseller',
    'Hallelujah, Yesterday', 'Ropa ligera y cómoda'
),
(7, 'Curiosa y perfeccionista', 'Llevar diario de laboratorio, correr',
    'Descubrimientos científicos', 'Error en resultados', 'Música instrumental', 'Críticas injustas',
    'Lectura científica, ajedrez', 'Muy alto (investigación avanzada)', 'Dirigir centro de investigación',
    'E=mc² (instrumental), Shine On You Crazy Diamond', 'Blazer y camisa blanca'
);

INSERT INTO contactData (idPaciente, contactName, contactFirstSurname, contactSecondSurname,contactAddress, contactEmail, contactTelecom, curatela, deFactoGuardian) VALUES
(2, 'Ana Ruiz', 'Ruiz', 'Sánchez', 'C/ Olivo 12, Sevilla',  'ana_ruiz@example.com', '600111222', 'Ninguna', 'Hijo mayor'),
(3, 'María López', 'López', 'Martín', 'Av. Los Pinos 5, Bilbao', 'maria_lopez@correo.com', '600333444', 'Tutela compartida', 'Abuela materna'),
(4, 'Juan González', 'González', 'Vidal', 'C/ Luna 23, Zaragoza', 'juan_gonzalez@empresa.com', '600555666', 'Ninguna', 'Hermana mayor'),
(5, 'Pilar Soto', 'Soto', 'Ruiz', 'Pº Sta. Catalina 8, Murcia','pilar_soto@correo.org', '600777888', 'Tutela legal por orfandad','Hermana adoptiva'),
(6, 'Óscar Gutiérrez','Gutiérrez','López', 'C/ San Roque 19, Málaga','oscar_gutierrez@correo.net', '600999000', 'Ninguna', 'Esposa'),
(7, 'David Navarro', 'Navarro', 'Morales', 'C/ Naranjo 47, Valladolid','david_navarro@correo.edu', '601111222', 'Ninguna', 'Hija menor');

INSERT INTO mainSanitaryData (idPaciente, mainIllness, allergies, otherIllness) VALUES
(2, 'Hipertensión',         'Polvo doméstico',       'Dolor de espalda crónico'),
(3, 'Diabetes tipo 2',      'Lactosa',               'Colesterol alto'),
(4, 'Asma crónico',         'Árboles (polen)',       'Sinusitis frecuente'),
(5, 'Cáncer en remisión',   'Ninguna',               'Osteoporosis'),
(6, 'Depresión crónica',    'Alergia a penicilina',  'Migrañas intensas'),
(7, 'Artrosis de rodilla',  'Ninguna',               'Tendinitis de hombro');

INSERT INTO pharmacy (idSanitary, treatment, regularPharmacy, visitFrequency, paymentMethod) VALUES
(2, 'Losartán 50mg diario',    'Farmacia San Jorge',       'Mensual',  'S'),
(3, 'Metformina 500mg cada 12h','Farmacia Bilbao Centro',    'Bimestral','P'),
(4, 'Salbutamol inhalador',     'Farmacia El Pilar',         'Cada 3 meses','S'),
(5, 'Tamoxifeno 20mg',          'Farmacia La Cruz',          'Mensual',  'D'),
(6, 'Sertralina 50mg',          'Farmacia Tropical',         'Mensual',  'S'),
(7, 'Celecoxib 200mg',          'Farmacia Castilla',         'Cada 2 meses','P');

INSERT INTO nursingMedicine (idSanitary, nutritionalSituation, sleepQuality, fallRisks, mobilityNeeds, healthPreferences) VALUES
(2, 'Dieta baja en sal',       'Sueño interrumpido',  'Medio', 'Bastón ocasional',   'Medicina natural'),
(3, 'Control estricto de calorías','Sueño regular', 'Bajo', 'Sin ayudas',          'Suplementos vitamínicos'),
(4, 'Dieta rica en antioxidantes','Sueño ligero',   'Alto', 'Nebulizador nocturno','Tratamientos inhalatorios'),
(5, 'Dieta alta en calcio',      'Sueño agitado',    'Medio','Muletas cuando sale', 'Terapia física regular'),
(6, 'Dieta equilibrada',         'Sueño irregular',  'Alto', 'Cama elevada',       'Psicoterapia semestral'),
(7, 'Dieta baja en grasas',      'Sueño profundo',   'Medio','Silla de ruedas para distancias largas', 'Rehabilitación kinésica');

INSERT INTO socialEducationOccupationalTherapy (idSanitary, cognitiveAbilities, affectiveCapacity, behaviorCapacity,collaborationLevel, autonomyLevel, groupParticipation) VALUES
(2, 'Reducidas ligeramente', 'Estable',    'Cooperativo',  'Alto',    'Autónomo supervisado',  'Asiste a talleres semanales'),
(3, 'Bien desarrolladas',    'Variable',   'Reservada',    'Medio',   'Autónomo',            'Participa en club de lectura'),
(4, 'Disminuidas por asma',   'Buena',      'Actitud positiva','Alto', 'Semi‐independiente',    'Participa en grupo de manualidades'),
(5, 'Levemente reducidas',   'Inestable',  'Creativa',     'Medio',   'Semi‐autónoma',        'Miembro activo de grupo de arte'),
(6, 'Disminuidas por depresión','Variable','Colaborativa',  'Bajo',  'Asistida',            'Taller de escritura mensual'),
(7, 'Reducidas por artrosis', 'Estable',   'Reservada',     'Medio',   'Autónomo supervisado',  'Siembra en huerto comunitario');

INSERT INTO socialWork (idSanitary, residentAndRelationship, petNameAndBreedPet, resources, legalSupport) VALUES
(2, 'Vive con hijo y madre',    'Nina - Pas Sheltie',  'Pensión mínima y ayuda social',       'Asesoría familiar básica'),
(3, 'Vive con abuela y hermanas','Toby - Mestizo',     'Negocio familiar pequeño',            'Asesoría fiscal puntual'),
(4, 'Vive con esposa e hijo',    'No tiene',           'Sueldo estable como ingeniero',       'Asesoría laboral estándar'),
(5, 'Reside en casa con hija',   'Luna - Pastor Alemán','Becas artísticas y pensión',          'Ninguna actualmente'),
(6, 'Vive con esposo e hijos',   'No tiene',           'Ambos trabajan (esposa e hijo)',      'Atención psicológica comunitaria'),
(7, 'Vive con esposa e hija',    'Max - Bóxer',         'Salario de investigadora',             'Beca de investigación');

INSERT INTO kitchenHygiene (idSanitary, favouriteFood, dietaryRestrictions, confortAdvices, routine, carePlan) VALUES
(2, 'Gazpacho',         'Baja en sal',                  'Mantener ventilación adecuada',    'Cocina cada mañana',     'Revisión dietética mensual'),
(3, 'Paella',           'Sin lactosa',                  'Cocinar con supervisión familiar', 'Planificación semanal',  'Chequeo metabólico trimestral'),
(4, 'Sopa de pollo',    'Sin gluten',                   'Usar utensilios antialérgenos',    'Cocinar 3 veces por semana','Consulta nutricional bimensual'),
(5, 'Pasta integral',   'Reducir azúcares',             'Evitar aceites saturados',         'Preparar comida en lotes', 'Seguimiento de densidad ósea'),
(6, 'Ensalada mixta',   'Sin penicilina (ingredientes)', 'Cocinar en horario estable',       'Cocinar 5 días por semana','Apoyo psicológico mensual'),
(7, 'Verduras al vapor', 'Baja en grasas',               'Mantener orden en cocina',         'Cocina cada día temprano','Fisioterapia semanal');

INSERT INTO otherData (idSanitary, professionalNotes) VALUES
(2, 'Paciente colabora en programas educativos comunitarios. Se recomienda seguimiento psicológico cada 6 meses.'),
(3, 'Alta motivación para emprender, requiere apoyo en gestión financiera.'),
(4, 'Se sugiere control respiratorio bimestral y evaluación psicológica por asma.'),
(5, 'Muy receptivo a terapias artísticas. Monitoreo de densidad ósea cada año.'),
(6, 'Actualmente en tratamiento por depresión. Alto riesgo de reingreso si falta adherencia.'),
(7, 'Destaca por resiliencia, sugerir participación en grupos de apoyo para enfermedad crónica.');

