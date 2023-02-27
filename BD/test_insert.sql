-- Active: 1677486538660@@127.0.0.1@3306@soutien
insert into SONDAGE values(1,'url1');

insert into MATIERE values(100, "maths");
insert into MATIERE values (150, "python");

insert into QCM values(2,'python','urlq1',100,STR_TO_DATE('2022/10/22','%Y/%m/%d'),STR_TO_DATE('2022/10/24','%Y/%m/%d'));

insert into ELEVE values(1,"jupilliat", "paulo",12,13);
insert into ELEVE values(2,"lang", "maxime",12,13);
insert into ELEVE values(3,"manach", "erwan",12,13);

insert into PROF values(10, "arzouz","julien","juju@gmail.com" );
insert into PROF values(11, "ADOBET","CHRISTINE","j@gmail.com" );

insert into PROF VALUES(12,"ESPINAS","Guilaine","G@gmail.com" );

 


insert into SOUTENIR VALUES(12, 100);
insert into SOUTENIR values (10,100);
insert into SOUTENIR values (10,150);
-- trigger2
insert into SOUTENIR values (11,150);
insert into SOUTENIR values (11,100);
--



insert into ORAUX values (2,"oral2",4,100,10,STR_TO_DATE('2022/10/22','%Y/%m/%d'));
insert into ORAUX values(1,"oral1",2,150,10,STR_TO_DATE('2022/10/22','%Y/%m/%d'));
-- trigger2
insert into ORAUX values(3,"oral3",5,150,12,STR_TO_DATE('2022/10/25','%Y/%m/%d'));
-- sencé retourner le pb car le prof 10 n'est pas capable de faire le cours 150

-- trigger3
insert into ORAUX values(5,"ORAL5",3,100,12,STR_TO_DATE('2022/10/20','%Y/%m/%d'));
-- FAIRE DES UPDATES SUR LES ORAUX SQLACHEMY POUR AJOUTER DES PROFESSEURS AUX ORAUX

insert into EST_DISPONIBLE values(10,1);
insert into EST_DISPONIBLE values(10,3);
insert into EST_DISPONIBLE values(11,2);


insert into RESULTAT VALUES (10.5,2,1);

insert into REPSONDAGE values("oui", "maths", "j'aime bien les maths mais j'ai du mal",STR_TO_DATE('2022/10/21','%Y/%m/%d'),1,1);

insert into PARTICIPE values("paul s'améliore pas dutout en maths ce bouffon", 1, 2);
insert into PARTICIPE values("maxime s'améliore en maths", 2, 2);


-- insertion de test trigger max_etu_oraux
insert into PARTICIPE values("paul s'améliore en maths", 1, 1);
insert into PARTICIPE values("maxime s'améliore en maths", 2, 1);
insert into PARTICIPE values("erwan s'améliore en maths", 3, 1);

insert into USER VALUES("admin", "admin", 1);


