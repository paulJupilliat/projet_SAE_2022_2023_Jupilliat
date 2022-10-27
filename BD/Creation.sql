DROP TABLE EST_DISPONIBLE;
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
    idMatiere INT,
    dateDebut DATE,
    dateFin DATE,
    Primary Key(idQCM),
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
    dateOral DATE,
    Primary Key(idOral),
    FOREIGN KEY (idMatiere) REFERENCES MATIERE(idMatiere),
    FOREIGN KEY (idProf) REFERENCES PROF(idProf)
);

CREATE TABLE RESULTAT (
    note DECIMAL (6,2),
    idQCM INT,
    numEtu INT,
    Primary Key(numEtu,idQCM),
    FOREIGN KEY(numEtu) REFERENCES ELEVE(numEtu),
    FOREIGN KEY(idQCM) REFERENCES QCM(idQCM)
);

CREATE TABLE REPSONDAGE (
    participation VARCHAR(255),
    matiere VARCHAR(255),
    commentaire VARCHAR(255),
    dateSondage DATE,
    numEtu INT,
    idSondage INT,
    idOral INT,
    Primary Key(numEtu,idSondage),
    FOREIGN KEY(numEtu) REFERENCES ELEVE(numEtu),
    FOREIGN KEY (idOral) REFERENCES ORAUX(idOral)
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





-- delimiter |

-- create or replace trigger max_etu_oraux before insert on PARTICIPE for each row
-- BEGIN 
--     declare mes VARCHAR(100) default '';
--     declare nombreEle int; 
--     declare eleMax int;
--     select nbEleveMax into eleMax from ORAUX where ORAUX.idOral = new.idOral;
--     select count(numEtu) into nombreEle from PARTICIPE where PARTICIPE.idOral = new.idOral; 
--     if nombreEle+1 > eleMax then 
--         set mes = concat("l'oral ",new.idOral," ne peut pas etre créé car il comporte plus que ", eleMax ," étudiants");
--         signal SQLSTATE '45000' set MESSAGE_TEXT = mes;
--     end if ;
-- end |
-- delimiter ;











-- un profs a un oral doit etre en capacite de faire la matiere de l'oral

-- delimiter |
-- create or replace trigger prof_capable_oraux before insert on ORAUX for each row
-- BEGIN 
--     declare matiere_possible VARCHAR(25) default '';
--     declare matiere_oral VARCHAR(25) default '';
--     declare messa VARCHAR(100) default '';
--     declare fini boolean DEFAULT false;
--     declare nomProfActu VARCHAR(100);
--     declare peut_faire boolean default false;
--     declare matiere_prof int;
--     declare lesMatieres cursor for
--         select idMatiere from SOUTENIR where new.idProf = SOUTENIR.idProf;
--     declare continue handler for not found set fini = true;
--     open lesMatieres;

--     while not fini do
--         fetch lesMatieres into matiere_prof;
--         if not fini then
--             if matiere_prof = new.idMatiere then
--                 set peut_faire = true;
--             end if;
--         end if;
--     end while;
--     close lesMatieres;
--     select nomProf into nomProfActu from PROF where PROF.idProf = new.idProf;
--     if not peut_faire then 
--         set messa = concat("le professeur ",nomProfActu,"  n'est pas en capacité d'assurer ce cours ");
--         signal SQLSTATE '45000' set MESSAGE_TEXT = messa;
--     end if ;
-- end |
-- delimiter ;

--trigger pour que le prof soit disponible pour l'oral


    -- si le prof ajouter dans l'oral n'est pas dans la table disponible avec le new.idOral alors je met le message d'erreur
-- delimiter |
-- create or replace trigger prof_dispo_oraux before insert on ORAUX for each row
-- BEGIN
--     declare messa VARCHAR(100) default '';
--     declare prof int;
--     if new.idProf is not null then 
--         select idProf into prof from EST_DISPONIBLE where new.idProf = EST_DISPONIBLE.idProf and new.idOral = EST_DISPONIBLE.idOral;
--         if prof is null then
--             set messa = concat("le professeur ",new.idProf," n'est pas disponible pour l'oral ",new.idOral);
--             signal SQLSTATE '45000' set MESSAGE_TEXT = messa;
--         end if;
--     end if ;
-- end |

-- create or replace trigger prof_dispo_oraux before update on ORAUX for each row
-- BEGIN
--     declare messa VARCHAR(100) default '';
--     declare prof int;
--     if new.idProf is not null then 
--         select idProf into prof from EST_DISPONIBLE where new.idProf = EST_DISPONIBLE.idProf and new.idOral = EST_DISPONIBLE.idOral;
--         if prof is null then
--             set messa = concat("le professeur ",new.idProf," n'est pas disponible pour l'oral ",new.idOral);
--             signal SQLSTATE '45000' set MESSAGE_TEXT = messa;
--         end if;
--     end if ;
-- end |
-- delimiter ;



























-- A VERIFIER 

























-- A VERIFIER 



-- trigger pour verifier que le prof n'a pas deja un oral a cette date

-- delimiter |
-- create or replace trigger prof_dispo_date before insert on ORAUX for each row
-- BEGIN 
--     declare messa VARCHAR(100) default '';
--     declare fini boolean DEFAULT false;
--     declare nomProfActu VARCHAR(100);
--     declare peut_faire boolean default false;
--     declare date_prof date;
--     declare lesDates cursor for
--         select dateOral from ORAUX where new.idProf = ORAUX.idProf;
--     declare continue handler for not found set fini = true;
--     open lesDates;

--     while not fini do
--         fetch lesDates into date_prof;
--         if not fini then
--             if date_prof = new.dateOral then
--                 set peut_faire = true;
--             end if;
--         end if;
--     end while;
--     close lesDates;
--     select nomProf into nomProfActu from PROF where PROF.idProf = new.idProf;
--     if peut_faire then 
--         set messa = concat("le professeur ",nomProfActu,"  a deja un oral a cette date ");
--         signal SQLSTATE '45000' set MESSAGE_TEXT = messa;
--     end if ;
-- end |
-- delimiter ;

-- -- trigger pour verifier qu'un commentaire doit etre redige par le prof qui a cree l'oral

-- delimiter |
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
-- delimiter ;
-- trigger pour que le prof faisant l'oral soit dispo
-- trigger
