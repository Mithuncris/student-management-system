-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: army_base
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance_attendance`
--

DROP TABLE IF EXISTS `attendance_attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance_attendance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(10) NOT NULL,
  `class_enrolled_id` bigint NOT NULL,
  `staff_id` bigint NOT NULL,
  `student_id` bigint NOT NULL,
  `period_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `attendance_attendanc_class_enrolled_id_23215c1f_fk_classes_c` (`class_enrolled_id`),
  KEY `attendance_attendance_staff_id_3bcf99e2_fk_users_customuser_id` (`staff_id`),
  KEY `attendance_attendance_student_id_94863613_fk_users_customuser_id` (`student_id`),
  KEY `attendance_attendance_period_id_71e6e302_fk_attendance_period_id` (`period_id`),
  CONSTRAINT `attendance_attendanc_class_enrolled_id_23215c1f_fk_classes_c` FOREIGN KEY (`class_enrolled_id`) REFERENCES `classes_class` (`id`),
  CONSTRAINT `attendance_attendance_period_id_71e6e302_fk_attendance_period_id` FOREIGN KEY (`period_id`) REFERENCES `attendance_period` (`id`),
  CONSTRAINT `attendance_attendance_staff_id_3bcf99e2_fk_users_customuser_id` FOREIGN KEY (`staff_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `attendance_attendance_student_id_94863613_fk_users_customuser_id` FOREIGN KEY (`student_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance_attendance`
--

LOCK TABLES `attendance_attendance` WRITE;
/*!40000 ALTER TABLE `attendance_attendance` DISABLE KEYS */;
/*!40000 ALTER TABLE `attendance_attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendance_period`
--

DROP TABLE IF EXISTS `attendance_period`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance_period` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `start_time` time(6) NOT NULL,
  `end_time` time(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance_period`
--

LOCK TABLES `attendance_period` WRITE;
/*!40000 ALTER TABLE `attendance_period` DISABLE KEYS */;
/*!40000 ALTER TABLE `attendance_period` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'HOD'),(2,'Staff');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (4,1,1),(5,1,2),(6,1,3),(7,1,4),(8,1,5),(9,1,6),(10,1,7),(11,1,8),(12,1,9),(13,1,10),(14,1,11),(15,1,12),(16,1,13),(17,1,14),(18,1,15),(19,1,16),(20,1,17),(21,1,18),(22,1,19),(23,1,20),(24,1,21),(25,1,22),(26,1,23),(27,1,24),(28,1,25),(29,1,26),(30,1,27),(31,1,28),(32,1,29),(33,1,30),(34,1,31),(35,1,32),(36,1,33),(37,1,34),(38,1,35),(39,1,36),(40,1,37),(41,1,38),(42,1,39),(43,1,40),(44,1,41),(45,1,42),(46,1,43),(47,1,44),(1,1,45),(2,1,46),(48,1,47),(49,2,1),(50,2,2),(51,2,3),(52,2,4),(53,2,21),(54,2,22),(55,2,23),(56,2,24),(57,2,25),(58,2,26),(59,2,27),(60,2,28),(61,2,29),(62,2,30),(63,2,31),(64,2,32),(65,2,33),(66,2,34),(67,2,35),(68,2,36),(69,2,41),(70,2,42),(71,2,43),(72,2,44),(3,2,45);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add Attendance Record',6,'add_attendance'),(22,'Can change Attendance Record',6,'change_attendance'),(23,'Can delete Attendance Record',6,'delete_attendance'),(24,'Can view Attendance Record',6,'view_attendance'),(25,'Can add Period',7,'add_period'),(26,'Can change Period',7,'change_period'),(27,'Can delete Period',7,'delete_period'),(28,'Can view Period',7,'view_period'),(29,'Can add class',8,'add_class'),(30,'Can change class',8,'change_class'),(31,'Can delete class',8,'delete_class'),(32,'Can view class',8,'view_class'),(33,'Can add student class enrollment',9,'add_studentclassenrollment'),(34,'Can change student class enrollment',9,'change_studentclassenrollment'),(35,'Can delete student class enrollment',9,'delete_studentclassenrollment'),(36,'Can view student class enrollment',9,'view_studentclassenrollment'),(37,'Can add user',10,'add_customuser'),(38,'Can change user',10,'change_customuser'),(39,'Can delete user',10,'delete_customuser'),(40,'Can view user',10,'view_customuser'),(41,'Can add internal marks',11,'add_internalmarks'),(42,'Can change internal marks',11,'change_internalmarks'),(43,'Can delete internal marks',11,'delete_internalmarks'),(44,'Can view internal marks',11,'view_internalmarks'),(45,'Can View Students',10,'can_view_students'),(46,'Can Manage Staff',10,'can_manage_staff'),(47,'Can View HOD',10,'can_view_hod'),(48,'Can add year',12,'add_year'),(49,'Can change year',12,'change_year'),(50,'Can delete year',12,'delete_year'),(51,'Can view year',12,'view_year'),(52,'Can add section',13,'add_section'),(53,'Can change section',13,'change_section'),(54,'Can delete section',13,'delete_section'),(55,'Can view section',13,'view_section');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes_class`
--

DROP TABLE IF EXISTS `classes_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes_class` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `teacher_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classes_class_teacher_id_e236cda2_fk_users_customuser_id` (`teacher_id`),
  CONSTRAINT `classes_class_teacher_id_e236cda2_fk_users_customuser_id` FOREIGN KEY (`teacher_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes_class`
--

LOCK TABLES `classes_class` WRITE;
/*!40000 ALTER TABLE `classes_class` DISABLE KEYS */;
/*!40000 ALTER TABLE `classes_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classes_studentclassenrollment`
--

DROP TABLE IF EXISTS `classes_studentclassenrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classes_studentclassenrollment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `class_enrolled_id` bigint NOT NULL,
  `student_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `classes_studentclass_class_enrolled_id_f9f8e6e8_fk_classes_c` (`class_enrolled_id`),
  KEY `classes_studentclass_student_id_06975c6d_fk_users_cus` (`student_id`),
  CONSTRAINT `classes_studentclass_class_enrolled_id_f9f8e6e8_fk_classes_c` FOREIGN KEY (`class_enrolled_id`) REFERENCES `classes_class` (`id`),
  CONSTRAINT `classes_studentclass_student_id_06975c6d_fk_users_cus` FOREIGN KEY (`student_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classes_studentclassenrollment`
--

LOCK TABLES `classes_studentclassenrollment` WRITE;
/*!40000 ALTER TABLE `classes_studentclassenrollment` DISABLE KEYS */;
/*!40000 ALTER TABLE `classes_studentclassenrollment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-10-07 04:44:12.905693','6','Dhinaharan',1,'[{\"added\": {}}]',10,1),(2,'2024-10-07 04:45:12.059578','6','Dhinaharan',2,'[{\"changed\": {\"fields\": [\"Role\"]}}]',10,1),(3,'2024-10-08 04:04:59.455258','6','Dhinaharan',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',10,1),(4,'2024-10-08 04:05:12.089051','6','Dhinaharan',2,'[]',10,1),(5,'2024-10-08 04:10:37.370468','6','Dhinaharan',2,'[]',10,1),(6,'2024-10-08 04:18:29.602342','6','Dhinaharan',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',10,1),(7,'2024-10-08 04:18:59.430341','1','HOD',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(8,'2024-10-08 04:22:21.935126','2','Staff',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(9,'2024-10-09 04:07:02.233464','3','ads_220085',3,'',10,1),(10,'2024-10-09 04:07:24.256375','4','Afiq',3,'',10,1),(11,'2024-10-09 04:07:44.039439','2','mithun',3,'',10,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(6,'attendance','attendance'),(7,'attendance','period'),(3,'auth','group'),(2,'auth','permission'),(8,'classes','class'),(9,'classes','studentclassenrollment'),(4,'contenttypes','contenttype'),(11,'internal','internalmarks'),(5,'sessions','session'),(10,'users','customuser'),(13,'users','section'),(12,'users','year');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-10-03 05:35:56.815623'),(2,'contenttypes','0002_remove_content_type_name','2024-10-03 05:35:56.896836'),(3,'auth','0001_initial','2024-10-03 05:35:57.236197'),(4,'auth','0002_alter_permission_name_max_length','2024-10-03 05:35:57.316210'),(5,'auth','0003_alter_user_email_max_length','2024-10-03 05:35:57.322260'),(6,'auth','0004_alter_user_username_opts','2024-10-03 05:35:57.331543'),(7,'auth','0005_alter_user_last_login_null','2024-10-03 05:35:57.340252'),(8,'auth','0006_require_contenttypes_0002','2024-10-03 05:35:57.344291'),(9,'auth','0007_alter_validators_add_error_messages','2024-10-03 05:35:57.351258'),(10,'auth','0008_alter_user_username_max_length','2024-10-03 05:35:57.360313'),(11,'auth','0009_alter_user_last_name_max_length','2024-10-03 05:35:57.367111'),(12,'auth','0010_alter_group_name_max_length','2024-10-03 05:35:57.386250'),(13,'auth','0011_update_proxy_permissions','2024-10-03 05:35:57.394252'),(14,'auth','0012_alter_user_first_name_max_length','2024-10-03 05:35:57.400684'),(15,'users','0001_initial','2024-10-03 05:35:57.782175'),(16,'admin','0001_initial','2024-10-03 05:35:57.950372'),(17,'admin','0002_logentry_remove_auto_add','2024-10-03 05:35:57.957916'),(18,'admin','0003_logentry_add_action_flag_choices','2024-10-03 05:35:57.966384'),(19,'classes','0001_initial','2024-10-03 05:35:58.016536'),(20,'attendance','0001_initial','2024-10-03 05:35:58.065503'),(21,'attendance','0002_initial','2024-10-03 05:35:58.140047'),(22,'attendance','0003_initial','2024-10-03 05:35:58.381610'),(23,'classes','0002_initial','2024-10-03 05:35:58.600596'),(24,'internal','0001_initial','2024-10-03 05:35:58.704122'),(25,'internal','0002_initial','2024-10-03 05:35:58.890660'),(26,'sessions','0001_initial','2024-10-03 05:35:58.931838'),(27,'users','0002_alter_customuser_options','2024-10-04 04:08:56.375943'),(28,'users','0003_auto_20241004_1338','2024-10-07 03:51:21.447612'),(29,'users','0004_customuser_department_customuser_section_and_more','2024-10-08 08:13:25.675778'),(30,'users','0005_section_year_alter_customuser_section_section_year_and_more','2024-10-08 08:42:44.383930'),(31,'users','0006_customuser_roll_number','2024-10-08 09:21:31.894827');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0vjsii4ict5i757vg78kl1ypq0ag00a2','e30:1swEit:E5CD8PlAtKR-Zn46cGQdfkpNqEMX3GHIuJPN2IPcvk8','2024-10-17 05:49:59.350769'),('dkixy7yr0ujzgvwrx7gy2folyvv7jv9y','.eJxVjEEOwiAQRe_C2pABOyAu3fcMZIBBqgaS0q6Md7dNutDtf-_9t_C0LsWvnWc_JXEVRpx-t0DxyXUH6UH13mRsdZmnIHdFHrTLsSV-3Q7376BQL1uNlBnAKQjD2RqLCS0DO0w6MzpSmC_a2QAxqEDZGoUaIg0IektSdOLzBdiCN5U:1sxfdd:FJBp-J-2Kvh5e1zizYEfi7wYvoJ_BNWF9yScNrFXOVU','2024-10-21 04:46:29.246833'),('gwvkinap10k8knk7ypkzkenywsq28wnm','.eJxVjL0OwiAYAN-F2ZBSKFBH9z4D-X5AqgaS0k7GdzckHXS9u9xbBDj2HI4Wt7CyuAorLr8MgZ6xdMEPKPcqqZZ9W1H2RJ62yaVyfN3O9m-QoeW-dQBJk3OGGMZhBq3VPKCaDE6GbUI_JMakGR2pefJj8hG9sdEpGklb8fkC8yc4Nw:1sy5qC:Y9RMulZl9ARSViXEzKMk6JLZaIRrFBjVOVFnhpH41Uw','2024-10-22 08:45:12.666555'),('tfd0hp8y2plw4gpj832t19vkwg4fo05i','.eJxVjL0OwiAYAN-F2ZBSKFBH9z4D-X5AqgaS0k7GdzckHXS9u9xbBDj2HI4Wt7CyuAorLr8MgZ6xdMEPKPcqqZZ9W1H2RJ62yaVyfN3O9m-QoeW-dQBJk3OGGMZhBq3VPKCaDE6GbUI_JMakGR2pefJj8hG9sdEpGklb8fkC8yc4Nw:1syO0C:4WoN05-r-x_7BIll4YMXPXnDu8HdX68G37NJWyQhbS8','2024-10-23 04:08:44.144089');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `internal_internalmarks`
--

DROP TABLE IF EXISTS `internal_internalmarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `internal_internalmarks` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `exam_name` varchar(50) NOT NULL,
  `marks` int NOT NULL,
  `class_enrolled_id` bigint NOT NULL,
  `staff_id` bigint NOT NULL,
  `student_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `internal_internalmar_class_enrolled_id_c03fc1c0_fk_classes_c` (`class_enrolled_id`),
  KEY `internal_internalmarks_staff_id_968d36e6_fk_users_customuser_id` (`staff_id`),
  KEY `internal_internalmar_student_id_c78e705c_fk_users_cus` (`student_id`),
  CONSTRAINT `internal_internalmar_class_enrolled_id_c03fc1c0_fk_classes_c` FOREIGN KEY (`class_enrolled_id`) REFERENCES `classes_class` (`id`),
  CONSTRAINT `internal_internalmar_student_id_c78e705c_fk_users_cus` FOREIGN KEY (`student_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `internal_internalmarks_staff_id_968d36e6_fk_users_customuser_id` FOREIGN KEY (`staff_id`) REFERENCES `users_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `internal_internalmarks`
--

LOCK TABLES `internal_internalmarks` WRITE;
/*!40000 ALTER TABLE `internal_internalmarks` DISABLE KEYS */;
/*!40000 ALTER TABLE `internal_internalmarks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser`
--

DROP TABLE IF EXISTS `users_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(10) NOT NULL,
  `department` varchar(100) DEFAULT NULL,
  `section_id` bigint DEFAULT NULL,
  `year_id` bigint DEFAULT NULL,
  `roll_number` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `roll_number` (`roll_number`),
  KEY `users_customuser_section_id_c2c632ce` (`section_id`),
  KEY `users_customuser_year_id_a720d3c5` (`year_id`),
  CONSTRAINT `users_customuser_section_id_c2c632ce_fk_users_section_id` FOREIGN KEY (`section_id`) REFERENCES `users_section` (`id`),
  CONSTRAINT `users_customuser_year_id_a720d3c5_fk_users_year_id` FOREIGN KEY (`year_id`) REFERENCES `users_year` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser`
--

LOCK TABLES `users_customuser` WRITE;
/*!40000 ALTER TABLE `users_customuser` DISABLE KEYS */;
INSERT INTO `users_customuser` VALUES (1,'pbkdf2_sha256$870000$QeDoO6FkoeF3vI8gBou5dE$nOnbrZlSoCZ/hoQukIZV9InP04FOeXnF72y1LxH7udM=','2024-10-09 04:06:32.893796',1,'army_admin','','','',1,1,'2024-10-03 05:37:12.162225','',NULL,NULL,NULL,NULL),(5,'pbkdf2_sha256$870000$rz0vqGO300MRjBrHFWFJ0Z$r6XaxQaXY20DJpaA5ESVq3eZyB00R8kLynzoGZF+B7w=','2024-10-04 08:28:20.693970',0,'Vada','','','thillumullupurpose@gmail.com',0,1,'2024-10-04 08:23:35.373525','hod',NULL,NULL,NULL,NULL),(6,'pbkdf2_sha256$870000$B5njCbNLTQxRuyWJ89W4Uq$534ymXywielAtOpAIpHQHM1X/qYd0OQ7f4KuhTTMbDg=','2024-10-09 04:08:44.138524',0,'Dhinaharan','','','',0,1,'2024-10-07 04:44:12.000000','hod',NULL,NULL,NULL,NULL),(13,'pbkdf2_sha256$870000$HjS4kiJ8I1cHaDWVd8Sy7B$5TkDBiU3gxpOD50Fmjd8vhJzu4ZMaVA9wlcF16FVcdk=',NULL,0,'mithun','Mithun','Raaj','',0,1,'2024-10-09 04:21:49.803749','student','AI&DS',9,3,'60'),(14,'pbkdf2_sha256$870000$7fVioE65wbqOQOniSQXYAQ$AjQvXIq1Gg7JScef1p8Ru7RRFKUZ9E00P2hKlFrpJfc=',NULL,0,'kamalaveni','Dr','Kamalaveni','',0,1,'2024-10-09 04:28:51.624874','staff','AI&DS',NULL,NULL,NULL);
/*!40000 ALTER TABLE `users_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser_groups`
--

DROP TABLE IF EXISTS `users_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  KEY `users_customuser_groups_group_id_01390b14_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_customuser_gro_customuser_id_958147bf_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `users_customuser_groups_group_id_01390b14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser_groups`
--

LOCK TABLES `users_customuser_groups` WRITE;
/*!40000 ALTER TABLE `users_customuser_groups` DISABLE KEYS */;
INSERT INTO `users_customuser_groups` VALUES (1,6,1);
/*!40000 ALTER TABLE `users_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_customuser_user_permissions`
--

DROP TABLE IF EXISTS `users_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  KEY `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_customuser_use_customuser_id_5771478b_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  CONSTRAINT `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_customuser_user_permissions`
--

LOCK TABLES `users_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_section`
--

DROP TABLE IF EXISTS `users_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_section` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `year_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_section_year_id_4f42e58f_fk_users_year_id` (`year_id`),
  CONSTRAINT `users_section_year_id_4f42e58f_fk_users_year_id` FOREIGN KEY (`year_id`) REFERENCES `users_year` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_section`
--

LOCK TABLES `users_section` WRITE;
/*!40000 ALTER TABLE `users_section` DISABLE KEYS */;
INSERT INTO `users_section` VALUES (1,'Section 1',1),(2,'Section 2',1),(3,'Section 3',1),(4,'Section 4',1),(5,'Section 1',2),(6,'Section 2',2),(7,'Section 3',2),(8,'Section 1',3),(9,'Section 2',3),(10,'Section 1',4);
/*!40000 ALTER TABLE `users_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_year`
--

DROP TABLE IF EXISTS `users_year`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_year` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_year`
--

LOCK TABLES `users_year` WRITE;
/*!40000 ALTER TABLE `users_year` DISABLE KEYS */;
INSERT INTO `users_year` VALUES (1,'I Year'),(2,'II Year'),(3,'III Year'),(4,'IV Year');
/*!40000 ALTER TABLE `users_year` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-09 12:18:24
