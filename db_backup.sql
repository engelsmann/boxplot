BEGIN TRANSACTION;
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
INSERT INTO "auth_group" VALUES(1,'Demo-gæster');
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "auth_group_permissions" VALUES(1,1,25);
INSERT INTO "auth_group_permissions" VALUES(2,1,29);
INSERT INTO "auth_group_permissions" VALUES(3,1,37);
INSERT INTO "auth_group_permissions" VALUES(4,1,33);
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO "auth_permission" VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES(5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES(6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES(8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES(9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES(10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES(11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES(12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES(13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES(14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES(15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES(16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES(21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES(22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES(23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES(24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES(25,7,'add_elev','Can add elev');
INSERT INTO "auth_permission" VALUES(26,7,'change_elev','Can change elev');
INSERT INTO "auth_permission" VALUES(27,7,'delete_elev','Can delete elev');
INSERT INTO "auth_permission" VALUES(28,7,'view_elev','Can view elev');
INSERT INTO "auth_permission" VALUES(29,8,'add_assesmentscores','Can add assesment scores');
INSERT INTO "auth_permission" VALUES(30,8,'change_assesmentscores','Can change assesment scores');
INSERT INTO "auth_permission" VALUES(31,8,'delete_assesmentscores','Can delete assesment scores');
INSERT INTO "auth_permission" VALUES(32,8,'view_assesmentscores','Can view assesment scores');
INSERT INTO "auth_permission" VALUES(33,9,'add_klasse','Can add klasse');
INSERT INTO "auth_permission" VALUES(34,9,'change_klasse','Can change klasse');
INSERT INTO "auth_permission" VALUES(35,9,'delete_klasse','Can delete klasse');
INSERT INTO "auth_permission" VALUES(36,9,'view_klasse','Can view klasse');
INSERT INTO "auth_permission" VALUES(37,10,'add_aflevering','Can add aflevering');
INSERT INTO "auth_permission" VALUES(38,10,'change_aflevering','Can change aflevering');
INSERT INTO "auth_permission" VALUES(39,10,'delete_aflevering','Can delete aflevering');
INSERT INTO "auth_permission" VALUES(40,10,'view_aflevering','Can view aflevering');
INSERT INTO "auth_permission" VALUES(41,8,'add_assesmentscore','Can add assesment score');
INSERT INTO "auth_permission" VALUES(42,8,'change_assesmentscore','Can change assesment score');
INSERT INTO "auth_permission" VALUES(43,8,'delete_assesmentscore','Can delete assesment score');
INSERT INTO "auth_permission" VALUES(44,8,'view_assesmentscore','Can view assesment score');
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
INSERT INTO "auth_user" VALUES(1,'pbkdf2_sha256$216000$MoQ1UIa11ngH$NI7T6RoZ1Y1rnxCuLNmqHJwsF1EIyeb2Rs3bzNyARCI=','2020-11-18 18:46:09.666777',1,'morten','Engelsmann','lumber.vision@gmail.com',1,1,'2020-11-11 21:24:42','Morten');
INSERT INTO "auth_user" VALUES(2,'pbkdf2_sha256$216000$7TKlfIRrWhoU$x0dlCC1ZkPXkRvjOurQrt6n4KlKFDh21kzIlmgtaAQI=',NULL,0,'boxplot','Boxplot','morten.engelsmann@outlook.dk',0,1,'2020-11-11 21:30:02','Bruger');
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "auth_user_groups" VALUES(1,2,1);
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "boxplot_aflevering" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "niveau" integer NOT NULL, "titel" varchar(30) NOT NULL, "frist" date NOT NULL, "klasse_id" integer NOT NULL REFERENCES "boxplot_klasse" ("id") DEFERRABLE INITIALLY DEFERRED, "oprettet" datetime NOT NULL, "senest" datetime NOT NULL);
INSERT INTO "boxplot_aflevering" VALUES(1,1,'Model af CoVID19','2020-11-10',3,'2020-11-12 16:57:11','2020-11-12 16:57:11');
CREATE TABLE "boxplot_assesmentscore" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "opg1" integer NOT NULL, "opg2" integer NOT NULL, "opg3" integer NOT NULL, "opg4" integer NOT NULL, "opg5" integer NOT NULL, "opg6" integer NOT NULL, "tankegang" integer NOT NULL, "fagsprog" integer NOT NULL, "cas" integer NOT NULL, "diagram" integer NOT NULL, "sammenhæng" integer NOT NULL, "konklusion" integer NOT NULL, "aflevering_id" integer NOT NULL REFERENCES "boxplot_aflevering" ("id") DEFERRABLE INITIALLY DEFERRED, "elev_id" integer NOT NULL REFERENCES "boxplot_elev" ("id") DEFERRABLE INITIALLY DEFERRED, "oprettet" datetime NOT NULL, "senest" datetime NOT NULL);
INSERT INTO "boxplot_assesmentscore" VALUES(1,3,1,3,3,3,2,2,4,2,4,1,4,1,2,'2020-11-12 16:57:11.494763','2020-11-12 16:57:11.561381');
INSERT INTO "boxplot_assesmentscore" VALUES(2,13,12,9,16,15,9,14,14,14,11,7,14,1,3,'2020-11-15 20:45:15.314145','2020-11-15 20:45:15.314159');
INSERT INTO "boxplot_assesmentscore" VALUES(3,15,13,14,15,15,19,15,17,17,15,10,17,1,4,'2020-11-15 20:45:15.771291','2020-11-15 20:45:15.771306');
INSERT INTO "boxplot_assesmentscore" VALUES(4,21,20,13,6,23,14,15,16,18,16,16,16,1,5,'2020-11-15 20:45:15.959916','2020-11-15 20:45:15.959930');
INSERT INTO "boxplot_assesmentscore" VALUES(5,16,14,10,13,14,11,13,13,16,16,8,12,1,6,'2020-11-15 20:45:16.191270','2020-11-15 20:45:16.191287');
INSERT INTO "boxplot_assesmentscore" VALUES(6,20,19,16,18,17,12,15,17,19,18,15,18,1,7,'2020-11-15 20:45:16.371207','2020-11-15 20:45:16.371222');
INSERT INTO "boxplot_assesmentscore" VALUES(7,18,6,6,11,10,6,9,9,11,11,7,10,1,8,'2020-11-15 20:45:16.582073','2020-11-15 20:45:16.582089');
INSERT INTO "boxplot_assesmentscore" VALUES(8,19,17,16,21,17,20,17,18,21,18,14,22,1,9,'2020-11-15 20:45:16.737479','2020-11-15 20:45:16.737493');
INSERT INTO "boxplot_assesmentscore" VALUES(9,24,11,16,19,10,8,12,12,20,16,14,14,1,10,'2020-11-15 20:45:16.957031','2020-11-15 20:45:16.957045');
INSERT INTO "boxplot_assesmentscore" VALUES(10,18,17,16,22,20,9,15,17,19,17,14,20,1,11,'2020-11-15 20:45:17.116663','2020-11-15 20:45:17.116678');
INSERT INTO "boxplot_assesmentscore" VALUES(11,19,18,15,22,23,18,20,18,23,20,15,19,1,12,'2020-11-15 20:45:17.315193','2020-11-15 20:45:17.315208');
INSERT INTO "boxplot_assesmentscore" VALUES(12,12,12,12,12,9,10,11,12,10,13,8,13,1,13,'2020-11-15 20:45:17.468232','2020-11-15 20:45:17.468248');
INSERT INTO "boxplot_assesmentscore" VALUES(13,13,12,9,16,15,9,14,14,14,11,7,14,1,14,'2020-11-15 20:45:17.593597','2020-11-15 20:45:17.593612');
INSERT INTO "boxplot_assesmentscore" VALUES(14,15,13,14,15,15,19,15,17,17,15,10,17,1,15,'2020-11-15 20:45:17.768551','2020-11-15 20:45:17.768566');
INSERT INTO "boxplot_assesmentscore" VALUES(15,21,20,13,6,23,14,15,16,18,16,16,16,1,16,'2020-11-15 20:45:18.026213','2020-11-15 20:45:18.026228');
INSERT INTO "boxplot_assesmentscore" VALUES(16,16,14,10,13,14,11,13,13,16,16,8,12,1,17,'2020-11-15 20:45:18.171308','2020-11-15 20:45:18.171323');
INSERT INTO "boxplot_assesmentscore" VALUES(17,20,19,16,18,17,12,15,17,19,18,15,18,1,18,'2020-11-15 20:45:18.323587','2020-11-15 20:45:18.323602');
INSERT INTO "boxplot_assesmentscore" VALUES(18,18,6,6,11,10,6,9,9,11,11,7,10,1,19,'2020-11-15 20:45:18.534980','2020-11-15 20:45:18.534995');
INSERT INTO "boxplot_assesmentscore" VALUES(19,19,17,16,21,17,20,17,18,21,18,14,22,1,20,'2020-11-15 20:45:18.679261','2020-11-15 20:45:18.679277');
INSERT INTO "boxplot_assesmentscore" VALUES(20,24,11,16,19,10,8,12,12,20,16,14,14,1,21,'2020-11-15 20:45:18.834539','2020-11-15 20:45:18.834554');
INSERT INTO "boxplot_assesmentscore" VALUES(21,18,17,16,22,20,9,15,17,19,17,14,20,1,22,'2020-11-15 20:45:18.967998','2020-11-15 20:45:18.968013');
INSERT INTO "boxplot_assesmentscore" VALUES(22,19,18,15,22,23,18,20,18,23,20,15,19,1,23,'2020-11-15 20:45:19.115116','2020-11-15 20:45:19.115131');
INSERT INTO "boxplot_assesmentscore" VALUES(23,12,12,12,12,9,10,11,12,10,13,8,13,1,24,'2020-11-15 20:45:19.292651','2020-11-15 20:45:19.292666');
INSERT INTO "boxplot_assesmentscore" VALUES(24,13,12,9,16,15,9,14,14,14,11,7,14,1,25,'2020-11-15 20:45:19.434591','2020-11-15 20:45:19.434605');
CREATE TABLE "boxplot_elev" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "fulde_navn" varchar(70) NOT NULL, "klasse_id" integer NOT NULL REFERENCES "boxplot_klasse" ("id") DEFERRABLE INITIALLY DEFERRED, "oprettet" datetime NOT NULL);
INSERT INTO "boxplot_elev" VALUES(1,'Andersine Andersen',1,'2020-11-12 16:57:11.577333');
INSERT INTO "boxplot_elev" VALUES(2,'Sida Dida',2,'2020-11-12 16:57:11.577333');
INSERT INTO "boxplot_elev" VALUES(3,'Camilla Horserød',3,'2020-11-15 08:07:38.535206');
INSERT INTO "boxplot_elev" VALUES(4,'Camilla Vejlebyskov',3,'2020-11-15 08:07:39.118732');
INSERT INTO "boxplot_elev" VALUES(5,'Emma Oue',3,'2020-11-15 08:07:39.451991');
INSERT INTO "boxplot_elev" VALUES(6,'Helle Barup',3,'2020-11-15 08:07:39.674828');
INSERT INTO "boxplot_elev" VALUES(7,'Helle Byskov',3,'2020-11-15 08:07:39.938095');
INSERT INTO "boxplot_elev" VALUES(8,'Henrik Menstrup',3,'2020-11-15 08:07:40.240924');
INSERT INTO "boxplot_elev" VALUES(9,'Henrik Voer Hede',3,'2020-11-15 08:07:40.427063');
INSERT INTO "boxplot_elev" VALUES(10,'Ida Himmark Mark',3,'2020-11-15 08:07:40.618540');
INSERT INTO "boxplot_elev" VALUES(11,'Jens Febbersted',3,'2020-11-15 08:07:40.818557');
INSERT INTO "boxplot_elev" VALUES(12,'Jens Molshuse',3,'2020-11-15 08:07:40.982550');
INSERT INTO "boxplot_elev" VALUES(13,'Jørgen Hallenslev Gårde',3,'2020-11-15 08:07:41.174039');
INSERT INTO "boxplot_elev" VALUES(14,'Jørgen Normark',3,'2020-11-15 08:07:41.349027');
INSERT INTO "boxplot_elev" VALUES(15,'Jørgen Storå',3,'2020-11-15 08:07:41.504508');
INSERT INTO "boxplot_elev" VALUES(16,'Jørgen Trængstrup',3,'2020-11-15 08:07:41.629468');
INSERT INTO "boxplot_elev" VALUES(17,'Kirsten Dybdal',3,'2020-11-15 08:07:41.773865');
INSERT INTO "boxplot_elev" VALUES(18,'Kirsten Hjortegårde',3,'2020-11-15 08:07:42.075819');
INSERT INTO "boxplot_elev" VALUES(19,'Maria Skibsted Å',3,'2020-11-15 08:07:42.229498');
INSERT INTO "boxplot_elev" VALUES(20,'Mette Blushøj',3,'2020-11-15 08:07:42.482223');
INSERT INTO "boxplot_elev" VALUES(21,'Mette Tise Udflyttere',3,'2020-11-15 08:07:42.607123');
INSERT INTO "boxplot_elev" VALUES(22,'Peter Holmdrup',3,'2020-11-15 08:07:42.740387');
INSERT INTO "boxplot_elev" VALUES(23,'Peter Villendrup',3,'2020-11-15 08:07:42.995997');
INSERT INTO "boxplot_elev" VALUES(24,'William Magleholm',3,'2020-11-15 08:07:43.162549');
INSERT INTO "boxplot_elev" VALUES(25,'William Trævel Å',3,'2020-11-15 08:07:43.384767');
CREATE TABLE "boxplot_klasse" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "skole" varchar(70) NOT NULL, "navn" varchar(10) NOT NULL, "start_år" integer NOT NULL, "oprettet" datetime NOT NULL);
INSERT INTO "boxplot_klasse" VALUES(1,'Frederiksborg Gymnasium og HF','1a',2019,'2020-11-12 16:57:11.608780');
INSERT INTO "boxplot_klasse" VALUES(2,'Frederiksborg Gymnasium og HF','2p',2018,'2020-11-12 16:57:11.608780');
INSERT INTO "boxplot_klasse" VALUES(3,'Prøvens Gymnasium','1test',2020,'2020-11-12 16:57:11.608780');
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0));
INSERT INTO "django_admin_log" VALUES(1,'2020-11-11 21:28:42.546318','1','Demo-gæster','[{"added": {}}]',3,1,1);
INSERT INTO "django_admin_log" VALUES(2,'2020-11-11 21:30:02.807230','2','boxplot','[{"added": {}}]',4,1,1);
INSERT INTO "django_admin_log" VALUES(3,'2020-11-11 21:31:03.920402','2','boxplot','[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES(4,'2020-11-11 21:31:59.541607','1','morten','[{"changed": {"fields": ["First name", "Last name"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES(5,'2020-11-11 21:41:14.006668','1','''Model af CoVID19'', 2p (2018/1) Frederiksborg Gymnasium og HF, senest: 2020-11-10','[{"changed": {"fields": ["Afleveringsfrist"]}}]',10,1,2);
INSERT INTO "django_admin_log" VALUES(6,'2020-11-11 21:41:53.622016','1','''Model af CoVID19'', 2p (2018/2) Frederiksborg Gymnasium og HF, senest: 2020-11-10','[{"changed": {"fields": ["Klassetrin for aflevering"]}}]',10,1,2);
INSERT INTO "django_admin_log" VALUES(7,'2020-11-15 17:15:20.008324','48','William Trævel Å, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(8,'2020-11-15 17:15:20.141918','47','William Magleholm, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(9,'2020-11-15 17:15:20.344557','46','Peter Villendrup, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(10,'2020-11-15 17:15:20.542411','45','Peter Holmdrup, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(11,'2020-11-15 17:15:20.697271','44','Mette Tise Udflyttere, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(12,'2020-11-15 17:15:20.830710','43','Mette Blushøj, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(13,'2020-11-15 17:15:20.964119','42','Maria Skibsted Å, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(14,'2020-11-15 17:15:21.152851','41','Kirsten Hjortegårde, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(15,'2020-11-15 17:15:21.286225','40','Kirsten Dybdal, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(16,'2020-11-15 17:15:21.497242','39','Jørgen Trængstrup, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(17,'2020-11-15 17:15:21.719348','38','Jørgen Storå, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(18,'2020-11-15 17:15:21.941912','37','Jørgen Normark, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(19,'2020-11-15 17:15:22.185946','36','Jørgen Hallenslev Gårde, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(20,'2020-11-15 17:15:22.430978','35','Jens Molshuse, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(21,'2020-11-15 17:15:22.687505','34','Jens Febbersted, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(22,'2020-11-15 17:15:22.930813','33','Ida Himmark Mark, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(23,'2020-11-15 17:15:23.119303','32','Henrik Voer Hede, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(24,'2020-11-15 17:15:23.363520','31','Henrik Menstrup, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(25,'2020-11-15 17:15:23.574949','30','Helle Byskov, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(26,'2020-11-15 17:15:23.807931','29','Helle Barup, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(27,'2020-11-15 17:15:23.963866','28','Emma Oue, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(28,'2020-11-15 17:15:24.219155','27','Camilla Vejlebyskov, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(29,'2020-11-15 17:15:24.585594','26','Camilla Horserød, 1test (2020), Prøvens Gymnasium','',7,1,3);
INSERT INTO "django_admin_log" VALUES(30,'2020-11-18 18:50:13.047528','1','''Model af CoVID19'', 1test (2020/2) Prøvens Gymnasium, senest: 2020-11-10','[{"changed": {"fields": ["Klasse"]}}]',10,1,2);
INSERT INTO "django_admin_log" VALUES(31,'2020-11-18 21:05:33.291103','1','''Model af CoVID19'', 1test (2020/1) Prøvens Gymnasium, senest: 2020-11-10','[{"changed": {"fields": ["Klassetrin for aflevering"]}}]',10,1,2);
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO "django_content_type" VALUES(1,'admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'auth','permission');
INSERT INTO "django_content_type" VALUES(3,'auth','group');
INSERT INTO "django_content_type" VALUES(4,'auth','user');
INSERT INTO "django_content_type" VALUES(5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(6,'sessions','session');
INSERT INTO "django_content_type" VALUES(7,'boxplot','elev');
INSERT INTO "django_content_type" VALUES(8,'boxplot','assesmentscore');
INSERT INTO "django_content_type" VALUES(9,'boxplot','klasse');
INSERT INTO "django_content_type" VALUES(10,'boxplot','aflevering');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2020-10-28 20:20:04.618192');
INSERT INTO "django_migrations" VALUES(2,'auth','0001_initial','2020-10-28 20:20:04.960108');
INSERT INTO "django_migrations" VALUES(3,'admin','0001_initial','2020-10-28 20:20:05.272432');
INSERT INTO "django_migrations" VALUES(4,'admin','0002_logentry_remove_auto_add','2020-10-28 20:20:05.601471');
INSERT INTO "django_migrations" VALUES(5,'admin','0003_logentry_add_action_flag_choices','2020-10-28 20:20:05.930629');
INSERT INTO "django_migrations" VALUES(6,'contenttypes','0002_remove_content_type_name','2020-10-28 20:20:06.132918');
INSERT INTO "django_migrations" VALUES(7,'auth','0002_alter_permission_name_max_length','2020-10-28 20:20:06.340985');
INSERT INTO "django_migrations" VALUES(8,'auth','0003_alter_user_email_max_length','2020-10-28 20:20:06.620155');
INSERT INTO "django_migrations" VALUES(9,'auth','0004_alter_user_username_opts','2020-10-28 20:20:06.878097');
INSERT INTO "django_migrations" VALUES(10,'auth','0005_alter_user_last_login_null','2020-10-28 20:20:07.116511');
INSERT INTO "django_migrations" VALUES(11,'auth','0006_require_contenttypes_0002','2020-10-28 20:20:07.345685');
INSERT INTO "django_migrations" VALUES(12,'auth','0007_alter_validators_add_error_messages','2020-10-28 20:20:07.525272');
INSERT INTO "django_migrations" VALUES(13,'auth','0008_alter_user_username_max_length','2020-10-28 20:20:07.691864');
INSERT INTO "django_migrations" VALUES(14,'auth','0009_alter_user_last_name_max_length','2020-10-28 20:20:07.945038');
INSERT INTO "django_migrations" VALUES(15,'auth','0010_alter_group_name_max_length','2020-10-28 20:20:08.171059');
INSERT INTO "django_migrations" VALUES(16,'auth','0011_update_proxy_permissions','2020-10-28 20:20:08.452472');
INSERT INTO "django_migrations" VALUES(17,'auth','0012_alter_user_first_name_max_length','2020-10-28 20:20:08.670278');
INSERT INTO "django_migrations" VALUES(18,'sessions','0001_initial','2020-10-28 20:20:08.818507');
INSERT INTO "django_migrations" VALUES(19,'boxplot','0001_initial','2020-10-29 21:45:59.703023');
INSERT INTO "django_migrations" VALUES(20,'boxplot','0002_auto_20201030_0343','2020-10-30 02:43:57.598328');
INSERT INTO "django_migrations" VALUES(21,'boxplot','0003_auto_20201112_1756','2020-11-12 16:57:11.631282');
INSERT INTO "django_migrations" VALUES(22,'boxplot','0004_auto_20201114_2032','2020-11-14 19:32:59.192421');
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "django_session" VALUES('mhcdqkocduezmztpk743f5w90sht78qh','.eJxVjDsOwjAQBe_iGlle_7Ap6XMGa9de4wBKpDipEHeHSCmgfTPzXiLhtra0dV7SWMRFgDj9boT5wdMOyh2n2yzzPK3LSHJX5EG7HObCz-vh_h007O1bG_AuBm0UYkHQJhB5rKwChHOlaDwiKeQcVEWw7EqIYIr1zmpiB1m8P90JN-w:1keC3X:sA0YL-sMWdKAL5zZDNhK-Q5ZH0v3bQtQHnbj-pcbDpY','2020-11-29 07:02:35.843058');
INSERT INTO "django_session" VALUES('seewxcuzf6xew4oe02e4dkqwr4xpb8z6','.eJxVjDsOwjAQBe_iGlle_7Ap6XMGa9de4wBKpDipEHeHSCmgfTPzXiLhtra0dV7SWMRFgDj9boT5wdMOyh2n2yzzPK3LSHJX5EG7HObCz-vh_h007O1bG_AuBm0UYkHQJhB5rKwChHOlaDwiKeQcVEWw7EqIYIr1zmpiB1m8P90JN-w:1kfST3:IoiMaSljaXiyWobdzLmCoq5Q8LHWO9L-FrjI-SOkyck','2020-12-02 18:46:09.910440');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('django_migrations',22);
INSERT INTO "sqlite_sequence" VALUES('django_admin_log',31);
INSERT INTO "sqlite_sequence" VALUES('django_content_type',10);
INSERT INTO "sqlite_sequence" VALUES('auth_permission',44);
INSERT INTO "sqlite_sequence" VALUES('auth_group',1);
INSERT INTO "sqlite_sequence" VALUES('auth_user',2);
INSERT INTO "sqlite_sequence" VALUES('auth_group_permissions',4);
INSERT INTO "sqlite_sequence" VALUES('auth_user_groups',1);
INSERT INTO "sqlite_sequence" VALUES('boxplot_aflevering',1);
INSERT INTO "sqlite_sequence" VALUES('boxplot_assesmentscore',24);
INSERT INTO "sqlite_sequence" VALUES('boxplot_elev',48);
INSERT INTO "sqlite_sequence" VALUES('boxplot_klasse',3);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "boxplot_aflevering_klasse_id_298e4538" ON "boxplot_aflevering" ("klasse_id");
CREATE INDEX "boxplot_assesmentscores_aflevering_id_df8ab979" ON "boxplot_assesmentscore" ("aflevering_id");
CREATE INDEX "boxplot_assesmentscores_elev_id_e700a960" ON "boxplot_assesmentscore" ("elev_id");
CREATE INDEX "boxplot_elev_klasse_id_498b40f4" ON "boxplot_elev" ("klasse_id");
COMMIT;
