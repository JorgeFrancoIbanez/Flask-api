-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('10197e745d2f');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `node`
--

DROP TABLE IF EXISTS `node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `node` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(140) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `mac` varchar(140) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `node`
--

LOCK TABLES `node` WRITE;
/*!40000 ALTER TABLE `node` DISABLE KEYS */;
INSERT INTO `node` VALUES (1,'default_name','0000-00-00 00:00:00',1,'MAC1234'),(2,'default_name2','0000-00-00 00:00:00',1,'qewwqe'),(3,'default_name','0000-00-00 00:00:00',1,'4376d7e73417ab88a232dd4afa83a664b139c29100f8e9153066f5e127146b60:3f35bc2578204a34b77868eb29a6fc11'),(4,'default_name','0000-00-00 00:00:00',1,'9d0b71d2295c7d4081fda64ec0b984deaee8bee30dbbc3cbed5ae7a34b9ef510:d9d442af9bb349fea2e6a97895bca525'),(5,'default_name','0000-00-00 00:00:00',1,'d5f5fb796a3c1967471cb35595bc8c607c0ce7f254fdde1f9c0fae6bfdd5a224:c51a3b95bb7049589934dc210e3603bf'),(6,'default_name','0000-00-00 00:00:00',1,'f3d01b5b0088c5b288a43707619c517925de57eb3b14f53420a01089029c9540:c4917ae2866e4198b8cc5a4ca480b060'),(7,'default_name','0000-00-00 00:00:00',1,'058530004cb9be8f08b05d216750691594bb4702040c1acf5c9e3e62de2e27b1:d60b7f432df54d10b2bc2e76fc89373b'),(8,'default_name','0000-00-00 00:00:00',1,'testmac'),(9,'pc','0000-00-00 00:00:00',5,'c8:5b:76:3d:10:e0');
/*!40000 ALTER TABLE `node` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `id` int(11) DEFAULT NULL,
  `message` varchar(140) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `node_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
INSERT INTO `post` VALUES (1,'this is a default message','0000-00-00 00:00:00',1,1),(2,'this is a default message','0000-00-00 00:00:00',1,1),(3,'this is a default message','0000-00-00 00:00:00',1,1),(4,'this is a default message','0000-00-00 00:00:00',5,5),(5,'this is a default message','0000-00-00 00:00:00',5,5),(6,'this is a default message','0000-00-00 00:00:00',5,5);
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) DEFAULT NULL,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `profile_image` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'jorge','jorge.franco@gmail.com','pbkdf2:sha256:50000$sagAyzHD$e434e9ff2064b5ffcd70e57e1252f8d6d0d53aae6ab2ff8d3af6156ee7a29803','0000-00-00 00:00:00',''),(2,'naty','naty@gmial.com','','0000-00-00 00:00:00',''),(3,'dani','dani@gmail.com','','0000-00-00 00:00:00',''),(4,'jorgefrancoibanez@gmail.com','jorgefrancoibanez@gmail.com','pbkdf2:sha256:50000$5m5cj0te$48c1ca5269541e3751fbf573641768810b478647aa5f92f42504e560e349737e','0000-00-00 00:00:00',''),(5,'js.mantilla128@gmail.com','js.mantilla128@gmail.com','pbkdf2:sha256:50000$zbbBfpYn$368e7e7d790929ae62c37b093a5c66dacf8dfa79518abe7eb7c53e47f9bb61b5','0000-00-00 00:00:00',''),(6,'test@test.com','testtest','','0000-00-00 00:00:00',''),(7,'test','test@test.com','','0000-00-00 00:00:00','');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-28 17:06:57
