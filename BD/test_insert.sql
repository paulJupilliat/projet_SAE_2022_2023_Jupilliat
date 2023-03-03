-- Active: 1677486538660@@127.0.0.1@3306@soutien
insert into SONDAGE values(1,'url1');

insert into MATIERE values(100, "maths");
insert into MATIERE values (150, "python");

insert into QCM values(2,'python','urlq1',100,'2022/10/22','2022/10/24');

insert into ELEVE values(1,"jupilliat", "paulo",12,13);
insert into ELEVE values(2,"lang", "maxime",12,13);
insert into ELEVE values(3,"manach", "erwan",12,13);

insert into PROF values(10, "arzouz","julien","juju@gmail.com" );
insert into PROF values(11, "ADOBET","CHRISTINE","j@gmail.com" );

 



insert into SOUTENIR values (10,100);
insert into SOUTENIR values (10,150);
-- trigger2
insert into SOUTENIR values (11,150);
insert into SOUTENIR values (11,100);
--



insert into ORAUX values (2,"oral2",4,100,10,'2022/10/22');
insert into ORAUX values(1,"oral1",2,150,10,'2022/10/22');
-- trigger2
insert into ORAUX values(3,"oral3",5,150,NULL,'2022/10/25');
-- sencé retourner le pb car le prof 10 n'est pas capable de faire le cours 150

-- trigger3
insert into ORAUX values(5,"ORAL5",3,100,NULL,'2022/10/20');
-- FAIRE DES UPDATES SUR LES ORAUX SQLACHEMY POUR AJOUTER DES PROFESSEURS AUX ORAUX

insert into EST_DISPONIBLE values(10,1);
insert into EST_DISPONIBLE values(10,3);
insert into EST_DISPONIBLE values(11,2);


insert into RESULTAT VALUES (10.5,2,1);

insert into REPSONDAGE values("oui", "maths", "j'aime bien les maths mais j'ai du mal",'2022/10/21',1,1,1);

insert into PARTICIPE values("paul s'améliore pas dutout en maths ce bouffon", 1, 2);
insert into PARTICIPE values("maxime s'améliore en maths", 2, 2);


-- insertion de test trigger max_etu_oraux
insert into PARTICIPE values("paul s'améliore en maths", 1, 1);
insert into PARTICIPE values("maxime s'améliore en maths", 2, 1);
insert into PARTICIPE values("erwan s'améliore en maths", 3, 1);

insert into periode VALUES(1,'2023/01/27','2023/10/22', 2);


insert into semaine VALUES(1,'2023/02/27','2023/03/05', 1);

-- {"id_semaine":2,"date_debut":"09/01/2023","date_fin":"15/01/2023"},{"id_semaine":3,"date_debut":"16/01/2023","date_fin":"22/01/2023"},
--     {"id_semaine":4,"date_debut":"23/01/2023","date_fin":"29/01/2023"}, {"id_semaine":5,"date_debut":"30/01/2023","date_fin":"05/02/2023"},
--     {"id_semaine":6,"date_debut":"06/02/2023","date_fin":"12/02/2023"},{"id_semaine":7,"date_debut":"13/02/2023","date_fin":"19/02/2023"},
--     {"id_semaine":8,"date_debut":"20/02/2023","date_fin":"26/02/2023"},{"id_semaine":9,"date_debut":"27/02/2023","date_fin":"05/03/2023"

insert into semaine VALUES(2,'2023/01/09','2023/01/15', 1);
insert into semaine VALUES(3,'2023/01/16','2023/01/22', 1);
insert into semaine VALUES(4,'2023/01/23','2023/01/29', 1);
insert into semaine VALUES(5,'2023/01/30','2023/02/05', 1);
insert into semaine VALUES(6,'2023/02/06','2023/02/12', 1);
insert into semaine VALUES(7,'2023/02/13','2023/02/19', 1);
insert into semaine VALUES(8,'2023/02/20','2023/02/26', 1);
insert into semaine VALUES(9,'2023/02/27','2023/03/05', 1);
