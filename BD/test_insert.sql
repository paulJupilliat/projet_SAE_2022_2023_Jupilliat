insert into SONDAGE values(1,'url1');

insert into QCM values(11,'paul','urlQCM');

insert into ELEVE values(1,"jupilliat", "paulo",12,13);
insert into ELEVE values(2,"lang", "maxime",12,13);
insert into ELEVE values(3,"manach", "erwan",12,13);

insert into PROF values(10, "arzouz","julien","juju@gmail.com" );
insert into PROF values(11, "ADOBET","CHRISTINE","j@gmail.com" );

insert into MATIERE values(100, "maths");
--trigger2
insert into MATIERE values (150, "python");
-- 



insert into SOUTENIR values (10,100);
--trigger2
insert into SOUTENIR values (11,150);
insert into SOUTENIR values (11,100);
--



insert into ORAUX values (2,"oral2",4,100,NULL);
insert into ORAUX values(1,"oral1",2,100,NULL);
--trigger2
insert into ORAUX values(3,"oral3",5,150,NULL);
-- sencé retourner le pb car le prof 10 n'est pas capable de faire le cours 150

-- trigger3
insert into ORAUX values(5,"ORAL5",3,100,NULL);
-- FAIRE DES UPDATES SUR LES ORAUX SQLACHEMY POUR AJOUTER DES PROFESSEURS AUX ORAUX

insert into EST_DISPONIBLE values(10,1);
insert into EST_DISPONIBLE values(10,3);
insert into EST_DISPONIBLE values(11,2);


insert into RESULTAT VALUES (10.5,11,1);

insert into REPSONDAGE values("oui", "maths", "j'aime bien les maths mais j'ai du mal",1,1,1);

insert into PARTICIPE values("paul s'améliore en maths", 1, 2);
insert into PARTICIPE values("maxime s'améliore en maths", 2, 2);


------------------------------------------------- insertion de test trigger max_etu_oraux
insert into PARTICIPE values("paul s'améliore en maths", 1, 1);
insert into PARTICIPE values("maxime s'améliore en maths", 2, 1);
insert into PARTICIPE values("erwan s'améliore en maths", 3, 1);




