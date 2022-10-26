DROP TABLE SOUTENIR;
DROP TABLE PARTICIPE;
DROP TABLE REPSONDAGE;
DROP TABLE RESULTAT;
DROP TABLE ORAUX;
DROP TABLE MATIERE;
DROP TABLE PROF;
DROP TABLE ELEVE;
DROP TABLE QCM;
DROP TABLE SONDAGE;


CREATE TABLE SONDAGE (
    idSondage INT,
    urlSondage VARCHAR(255),
    Primary Key (idSondage)
);

CREATE TABLE QCM (
    idQCM INT,
    nomQCM VARCHAR(255),
    urlQCM VARCHAR(255),
    Primary Key(idQCM)
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

CREATE TABLE MATIERE (
    idMatiere INT,
    nomMatiere VARCHAR(255),
    Primary Key (idMatiere)
);

CREATE TABLE ORAUX (
    idOral INT,
    nomOral VARCHAR(255),
    nbEleveMax INT(10),
    idMatiere int(10),
    idProf int(10),
    Primary Key(idOral),
    FOREIGN KEY (idMatiere) REFERENCES MATIERE(idMatiere),
    FOREIGN KEY (idProf) REFERENCES PROF(idProf)
);

CREATE TABLE RESULTAT (
    note DECIMAL (6,2),
    idQCM INT,
    idEleve INT,
    Primary Key(idEleve,idQCM),
    FOREIGN KEY(idEleve) REFERENCES ELEVE(numEtu),
    FOREIGN KEY(idQCM) REFERENCES QCM(idQCM)
);

CREATE TABLE REPSONDAGE (
    participation VARCHAR(255),
    matiere VARCHAR(255),
    commentaire VARCHAR(255),
    idEleve INT,
    idSondage INT,
    idOral INT,
    Primary Key(idEleve,idSondage),
    FOREIGN KEY(idEleve) REFERENCES ELEVE(numEtu),
    FOREIGN KEY (idOral) REFERENCES ORAUX(idOral)
);

CREATE TABLE PARTICIPE (
    commentaire VARCHAR(255),
    idEleve INT,
    idOral INT,
    Primary Key(idEleve,idOral),
    FOREIGN KEY (idEleve) REFERENCES ELEVE(numEtu),
    FOREIGN KEY (idOral) REFERENCES ORAUX(idOral)
);

CREATE TABLE SOUTENIR(
    idProf int(10),
    idMatiere int(10),
    Primary Key(idProf,idMatiere),
    FOREIGN KEY (idMatiere) REFERENCES MATIERE(idMatiere),
    FOREIGN KEY (idProf) REFERENCES PROF(idProf)
);





delimiter |

create or replace trigger max_etu_oraux before insert on PARTICIPE for each row
BEGIN 
    declare mes VARCHAR(100) default '';
    declare nombreEle int; 
    declare eleMax int;
    select nbEleveMax into eleMax from ORAUX where ORAUX.idOral = new.idOral;
    select count(idEleve) into nombreEle from PARTICIPE where PARTICIPE.idOral = new.idOral; 
    if nombreEle+1 > eleMax then 
        set mes = concat("l'oral ne peut pas etre créé car il comporte plus que ", eleMax ," étudiants");
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
    end if ; 
end |
delimiter ;












-- un profs a un oral doit doit etre en capacite de faire la matiere de l'oral

-- delimiter |
-- create or replace trigger prof_dispo_oraux before insert on ORAUX for each row
-- BEGIN 
--     declare matiere_possible VARCHAR(25) default '';
--     declare matiere_oral VARCHAR(25) default '';
--     declare messa VARCHAR(100) default '';
--     declare professeur int(10);
--     select idMatiere, idProf into matiere_oral, professeur from ORAUX where new.idMatiere in (select idMatiere from SOUTENIR where SOUTENIR.idProf = ORAUX.idProf) and ORAUX.idMatiere = new.idMatiere;
--     if idMatiere is null then 
--         set messa = concat("le professeur : " + professeur + " n'est pas en capacité d'assurer ce cours ");
--         signal SQLSTATE '45000' set MESSAGE_TEXT = messa;
--     end if ;
-- end |
-- delimiter ;

