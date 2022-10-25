DROP TABLE PARTICIPE;
DROP TABLE REPSONDAGE;
DROP TABLE RESULTAT;
DROP TABLE DATE;
DROP TABLE ORAUX;
DROP TABLE MATIERE;
DROP TABLE PROF;
DROP TABLE ELEVE;
DROP TABLE QCM;
DROP TABLE SONDAGE;


CREATE TABLE SONDAGE (
    idSondage INT NOT NULL AUTO_INCREMENT,
    urlSondage VARCHAR(255) NOT NULL,
    Primary Key (idSondage)
);

CREATE TABLE QCM (
    idQCM INT NOT NULL AUTO_INCREMENT,
    nomQCM VARCHAR(255),
    urlQCM VARCHAR(255),
    Primary Key(idQCM)
)

CREATE TABLE ELEVE  (
    numEtu INT NOT NULL AUTO_INCREMENT,
    nomEleve VARCHAR(255) NOT NULL,
    prenomEleve VARCHAR(255) NOT NULL,
    groupeS1 INT(10) NOT NULL,
    groupeS2 INT(10) NOT NULL,
    Primary Key (idEleve)
);

CREATE TABLE PROF (
    idProf INT NOT NULL AUTO_INCREMENT,
    nomProf VARCHAR(255) NOT NULL,
    prenomProf VARCHAR(255) NOT NULL,
    emailProf VARCHAR(255) NOT NULL,
    Primary Key (idProf)
);

CREATE TABLE MATIERE (
    idMatiere INT NOT NULL AUTO_INCREMENT,
    nomMatiere VARCHAR(255) NOT NULL,
    Primary Key (idMatiere)
);

CREATE TABLE ORAUX (
    idOral INT NOT NULL AUTO_INCREMENT,
    nomOral VARCHAR(255) NOT NULL,
    nbEleveMax INT(10) NOT NULL,
    Primary Key(idOral)
);

CREATE TABLE DATE (
    date DATE,
    Primary Key(date)
);

CREATE TABLE RESULTAT (
    note deicmal(6,2),
    idQCM INT NOT NULL AUTO_INCREMENT,
    idEleve INT NOT NULL AUTO_INCREMENT,
    Primary Key(idEleve,idQCM),
    FOREIGN KEY(idEleve) REFERENCES ELEVE(idEleve),
    FOREIGN KEY(idQCM) REFERENCES QCM(idQCM)
);

CREATE TABLE REPSONDAGE (
    participation VARCHAR(255),
    matiere VARCHAR(255),
    commentaire VARCHAR(255),
    idEleve INT NOT NULL AUTO_INCREMENT,
    idSondage INT NOT NULL AUTO_INCREMENT,
    Primary Key(idEleve,idSondage),
    FOREIGN KEY(idEleve) REFERENCES ELEVE(idEleve),
    FOREIGN KEY (idOral) REFERENCES ORAUX(idOral)
);

CREATE TABLE PARTICIPE (
    commentaire VARCHAR(255),
    idEleve INT NOT NULL AUTO_INCREMENT,
    idOral INT NOT NULL AUTO_INCREMENT,
    Primary Key(idEleve,idOral),
    FOREIGN KEY (idEleve) REFERENCES ELEVE(idEleve),
    FOREIGN KEY (idOral) REFERENCES ORAUX(idOral)
);
