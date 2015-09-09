-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: 10.9.1.188    Database: cf_7bc38f81_3a7c_496c_ab4d_f1aa4dcd0589
-- ------------------------------------------------------
-- Server version	5.6.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `a`
--

DROP TABLE IF EXISTS `a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `a` (
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a`
--

LOCK TABLES `a` WRITE;
/*!40000 ALTER TABLE `a` DISABLE KEYS */;
/*!40000 ALTER TABLE `a` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `id` int(11) DEFAULT NULL,
  `info` varchar(256) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES (0,'dasf0'),(1,'dasf1'),(2,'dasf2'),(3,'dasf3'),(4,'dasf4'),(5,'dasf5'),(6,'dasf6'),(7,'dasf7'),(8,'dasf8'),(9,'dasf9'),(10,'dasf10'),(11,'dasf11'),(12,'dasf12'),(13,'dasf13'),(14,'dasf14'),(15,'dasf15'),(16,'dasf16'),(17,'dasf17'),(18,'dasf18'),(19,'dasf19'),(20,'dasf20'),(21,'dasf21'),(22,'dasf22'),(23,'dasf23'),(24,'dasf24'),(25,'dasf25'),(26,'dasf26'),(27,'dasf27'),(28,'dasf28'),(29,'dasf29'),(30,'dasf30'),(31,'dasf31'),(32,'dasf32'),(33,'dasf33'),(34,'dasf34'),(35,'dasf35'),(36,'dasf36'),(37,'dasf37'),(38,'dasf38'),(39,'dasf39'),(40,'dasf40'),(41,'dasf41'),(42,'dasf42'),(43,'dasf43'),(44,'dasf44'),(45,'dasf45'),(46,'dasf46'),(47,'dasf47'),(48,'dasf48'),(49,'dasf49'),(50,'dasf50'),(51,'dasf51'),(52,'dasf52'),(53,'dasf53'),(54,'dasf54'),(55,'dasf55'),(56,'dasf56'),(57,'dasf57'),(58,'dasf58'),(59,'dasf59'),(60,'dasf60'),(61,'dasf61'),(62,'dasf62'),(63,'dasf63'),(64,'dasf64'),(65,'dasf65'),(66,'dasf66'),(67,'dasf67'),(68,'dasf68'),(69,'dasf69'),(70,'dasf70'),(71,'dasf71'),(72,'dasf72'),(73,'dasf73'),(74,'dasf74'),(75,'dasf75'),(76,'dasf76'),(77,'dasf77'),(78,'dasf78'),(79,'dasf79'),(80,'dasf80'),(81,'dasf81'),(82,'dasf82'),(83,'dasf83'),(84,'dasf84'),(85,'dasf85'),(86,'dasf86'),(87,'dasf87'),(88,'dasf88'),(89,'dasf89'),(90,'dasf90'),(91,'dasf91'),(92,'dasf92'),(93,'dasf93'),(94,'dasf94'),(95,'dasf95'),(96,'dasf96'),(97,'dasf97'),(98,'dasf98'),(99,'dasf99'),(0,'dasf0'),(1,'dasf1'),(2,'dasf2'),(3,'dasf3'),(4,'dasf4'),(5,'dasf5'),(6,'dasf6'),(7,'dasf7'),(8,'dasf8'),(9,'dasf9'),(10,'dasf10'),(11,'dasf11'),(12,'dasf12'),(13,'dasf13'),(14,'dasf14'),(15,'dasf15'),(16,'dasf16'),(17,'dasf17'),(18,'dasf18'),(19,'dasf19'),(20,'dasf20'),(21,'dasf21'),(22,'dasf22'),(23,'dasf23'),(24,'dasf24'),(25,'dasf25'),(26,'dasf26'),(27,'dasf27'),(28,'dasf28'),(29,'dasf29'),(30,'dasf30'),(31,'dasf31'),(32,'dasf32'),(33,'dasf33'),(34,'dasf34'),(35,'dasf35'),(36,'dasf36'),(37,'dasf37'),(38,'dasf38'),(39,'dasf39'),(40,'dasf40'),(41,'dasf41'),(42,'dasf42'),(43,'dasf43'),(44,'dasf44'),(45,'dasf45'),(46,'dasf46'),(47,'dasf47'),(48,'dasf48'),(49,'dasf49'),(50,'dasf50'),(51,'dasf51'),(52,'dasf52'),(53,'dasf53'),(54,'dasf54'),(55,'dasf55'),(56,'dasf56'),(57,'dasf57'),(58,'dasf58'),(59,'dasf59'),(60,'dasf60'),(61,'dasf61'),(62,'dasf62'),(63,'dasf63'),(64,'dasf64'),(65,'dasf65'),(66,'dasf66'),(67,'dasf67'),(68,'dasf68'),(69,'dasf69'),(70,'dasf70'),(71,'dasf71'),(72,'dasf72'),(73,'dasf73'),(74,'dasf74'),(75,'dasf75'),(76,'dasf76'),(77,'dasf77'),(78,'dasf78'),(79,'dasf79'),(80,'dasf80'),(81,'dasf81'),(82,'dasf82'),(83,'dasf83'),(84,'dasf84'),(85,'dasf85'),(86,'dasf86'),(87,'dasf87'),(88,'dasf88'),(89,'dasf89'),(90,'dasf90'),(91,'dasf91'),(92,'dasf92'),(93,'dasf93'),(94,'dasf94'),(95,'dasf95'),(96,'dasf96'),(97,'dasf97'),(98,'dasf98'),(99,'dasf9fdasfaer');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-09 23:45:11
