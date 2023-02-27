-- Active: 1677486538660@@127.0.0.1@3306@soutien
DROP TABLE EST_DISPONIBLE;
DROP TABLE SOUTENIR;
DROP TABLE PARTICIPE;
DROP TABLE REPSONDAGE;
DROP TABLE RESULTAT;
DROP TABLE ORAUX;
DROP TABLE PROF;
DROP TABLE ELEVE;
DROP TABLE USER;
DROP TABLE QCM;
DROP TABLE MATIERE;
DROP TABLE SONDAGE;


CREATE TABLE SONDAGE (
    idSondage INT,
    urlSondage VARCHAR(255),
    Primary Key (idSondage)
);

CREATE TABLE MATIERE (
    idMatiere INT,
    nomMatiere VARCHAR(255),
    Primary Key (idMatiere)
);

CREATE TABLE QCM (
    idQCM INT,
    nomQCM VARCHAR(255),
    urlQCM VARCHAR(255),
    idMatiere INT,
    dateDebut DATE,
    dateFin DATE,
    Primary Key (idQCM),
    Foreign Key (idMatiere) References MATIERE(idMatiere)
);

CREATE TABLE ELEVE  (
    numEtu INT(10),
    nomEleve VARCHAR(255),
    prenomEleve VARCHAR(255),
    groupeS1 INT(10),
    groupeS2 INT(10),
    Primary Key (numEtu)
);

CREATE TABLE PROF (
    idProf INT,
    nomProf VARCHAR(255),
    prenomProf VARCHAR(255),
    emailProf VARCHAR(255),
    Primary Key (idProf)
);

CREATE TABLE USER(
    username VARCHAR(255),
    pswd VARCHAR(255),
    estAdmin boolean,
    Primary KEY (username)
);


CREATE TABLE ORAUX (
    idOral INT,
    nomOral VARCHAR(255),
    nbEleveMax INT(10),
    idMatiere int(10),
    idProf int(10),
    dateOral DATE,
    Primary Key (idOral),
    FOREIGN KEY (idMatiere) REFERENCES MATIERE(idMatiere),
    FOREIGN KEY (idProf) REFERENCES PROF(idProf)
);

-- Rajouter l'année pour le resultat et pour les réponses sondages 

CREATE TABLE RESULTAT (
    note DECIMAL (6,2),
    idQCM INT,
    numEtu INT,
    Primary Key (numEtu,idQCM),
    FOREIGN KEY (numEtu) REFERENCES ELEVE(numEtu),
    FOREIGN KEY (idQCM) REFERENCES QCM(idQCM)
);

CREATE TABLE REPSONDAGE (
    participation VARCHAR(255),
    matiere VARCHAR(255),
    commentaire VARCHAR(255),
    dateSondage DATE,
    numEtu INT,
    idSondage INT,
    Primary Key(numEtu,idSondage,dateSondage),
    FOREIGN KEY(numEtu) REFERENCES ELEVE(numEtu)
);

CREATE TABLE PARTICIPE (
    commentaire VARCHAR(255),
    numEtu INT,
    idOral INT,
    Primary Key(numEtu,idOral),
    FOREIGN KEY (numEtu) REFERENCES ELEVE(numEtu),
    FOREIGN KEY (idOral) REFERENCES ORAUX(idOral)
);

CREATE TABLE SOUTENIR(
    idProf int(10),
    idMatiere int(10),
    Primary Key(idProf,idMatiere),
    FOREIGN KEY (idMatiere) REFERENCES MATIERE(idMatiere),
    FOREIGN KEY (idProf) REFERENCES PROF(idProf)
);

Create TABLE EST_DISPONIBLE(
    idProf int(10),
    idOral int(10),
    Primary Key(idProf,idOral),
    FOREIGN KEY (idProf) REFERENCES PROF(idProf),
    FOREIGN KEY (idOral) REFERENCES ORAUX(idOral)
);





delimiter |

CREATE TRIGGER max_etu_oraux 
BEFORE INSERT ON PARTICIPE 
FOR EACH ROW
BEGIN 
    DECLARE mes VARCHAR(100) DEFAULT '';
    DECLARE nombreEle INT; 
    DECLARE eleMax INT;
    SELECT nbEleveMax INTO eleMax FROM ORAUX WHERE ORAUX.idOral = NEW.idOral;
    SELECT COUNT(numEtu) INTO nombreEle FROM PARTICIPE WHERE PARTICIPE.idOral = NEW.idOral; 
    IF nombreEle + 1 > eleMax THEN 
        SET mes = CONCAT('l\'oral ', NEW.idOral, ' ne peut pas être créé car il comporte plus que ', eleMax ,' étudiants');
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = mes;
    END IF ;
END;
delimiter ;

-- un profs a un oral doit etre en capacite de faire la matiere de l'oral

delimiter |
DROP TRIGGER IF EXISTS prof_capable_oraux;
DELIMITER //
CREATE TRIGGER prof_capable_oraux BEFORE INSERT ON ORAUX FOR EACH ROW
BEGIN 
    DECLARE matiere_possible VARCHAR(25) DEFAULT '';
    DECLARE matiere_oral VARCHAR(25) DEFAULT '';
    DECLARE messa VARCHAR(100) DEFAULT '';
    DECLARE fini BOOLEAN DEFAULT false;
    DECLARE nomProfActu VARCHAR(100);
    DECLARE peut_faire BOOLEAN DEFAULT false;
    DECLARE matiere_prof INT;
    DECLARE nombreOral INT; 
    DECLARE prof INT;
    DECLARE lesMatieres CURSOR FOR SELECT idMatiere FROM SOUTENIR WHERE new.idProf = SOUTENIR.idProf;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fini = true;
    OPEN lesMatieres;

    WHILE NOT fini DO
        FETCH lesMatieres INTO matiere_prof;
        IF NOT fini THEN
            IF matiere_prof = new.idMatiere THEN
                SET peut_faire = true;
            END IF;
        END IF;
    END WHILE;
    CLOSE lesMatieres;
    SELECT nomProf INTO nomProfActu FROM PROF WHERE PROF.idProf = new.idProf;
    IF NOT peut_faire THEN 
        SET messa = CONCAT("le professeur ",nomProfActu," n'est pas en capacité d'assurer ce cours");
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = messa;
    END IF ;
    IF new.idProf IS NOT NULL THEN 
        SELECT idProf INTO prof FROM EST_DISPONIBLE WHERE new.idProf = EST_DISPONIBLE.idProf AND new.idOral = EST_DISPONIBLE.idOral;
        IF prof IS NOT NULL THEN
            SET messa = CONCAT("le professeur ",new.idProf," n'est pas disponible pour l'oral ",new.idOral);
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = messa;
        END IF;
    END IF ;
    SELECT COUNT(idOral) INTO nombreOral FROM ORAUX WHERE ORAUX.idProf = new.idProf AND ORAUX.dateOral = new.dateOral; 
    IF nombreOral > 1 THEN 
        SET messa = CONCAT("l'oral ne peut pas être créé car le prof comporte plus que 1 oral");
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = messa;
    END IF ;
END //
delimiter ;

-- trigger pour que le prof soit disponible pour l'oral


--si le prof ajouter dans l'oral n'est pas dans la table disponible avec le new.idOral alors je met le message d'erreur
-- trigger pour verifier qu'un commentaire doit etre redige par le prof qui a cree l'oral

delimiter |
-- create or replace trigger prof_commentaire before insert on REPSONDAGE for each row
-- BEGIN 
--     declare messa VARCHAR(100) default '';
--     declare fini boolean DEFAULT false;
--     declare nomProfActu VARCHAR(100);
--     declare peut_faire boolean default false;
--     declare idProfOral int;
--     declare lesProf cursor for
--         select idProf from ORAUX where new.idOral = ORAUX.idOral;
--     declare continue handler for not found set fini = true;
--     open lesProf;

--     while not fini do
--         fetch lesProf into idProfOral;
--         if not fini then
--             if idProfOral = new.numEtu then
--                 set peut_faire = true;
--             end if;
--         end if;
--     end while;
--     close lesProf;
--     select nomProf into nomProfActu from PROF where PROF.idProf = new.numEtu;
--     if not peut_faire then 
--         set messa = concat("le professeur ",nomProfActu,"  n'a pas cree cet oral ");
--         signal SQLSTATE '45000' set MESSAGE_TEXT = messa;
--     end if ;
-- end |
delimiter ;
-- trigger pour que le prof faisant l'oral soit dispo
-- trigger
