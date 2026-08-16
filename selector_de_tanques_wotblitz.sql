-- Habría que crear nuevas tablas para las clases, niveles, tipos y naciones, y cambiar los valores de las columnas de la tabla de tanques


-- MySQL dump 10.13  Distrib 8.0.45, for macos15 (x86_64)
--
-- Host: localhost    Database: selector_de_tanques_wotblitz
-- ------------------------------------------------------
-- Server version	9.6.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'fb43871a-23db-11f1-9dcc-276fb84d57cf:1-202';

--
-- Table structure for table `caracteristicas`
--

DROP TABLE IF EXISTS `caracteristicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caracteristicas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caracteristicas`
--

LOCK TABLES `caracteristicas` WRITE;
/*!40000 ALTER TABLE `caracteristicas` DISABLE KEYS */;
INSERT INTO `caracteristicas` VALUES (1,'Cañón convencional'),(2,'Cargador automático'),(3,'Recargador automático'),(4,'Daño por minuto'),(5,'Daño por disparo'),(6,'Penetración'),(7,'Tiempo de apuntado'),(8,'Dispersión'),(9,'Depresión del cañón'),(10,'Velocidad máxima'),(11,'Relación potencia/peso'),(12,'Puntos de vida'),(13,'Alcance de visión'),(14,'Camuflaje'),(15,'Blindaje de la torreta'),(16,'Blindaje del casco');
/*!40000 ALTER TABLE `caracteristicas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tanques`
--

DROP TABLE IF EXISTS `tanques`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tanques` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `nacion` varchar(15) DEFAULT NULL,
  `clase` varchar(10) DEFAULT NULL,
  `tier` varchar(4) DEFAULT NULL,
  `tipo` varchar(17) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64066 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tanques`
--

LOCK TABLES `tanques` WRITE;
/*!40000 ALTER TABLE `tanques` DISABLE KEYS */;
INSERT INTO `tanques` VALUES (10033,'WZ-132A','China','Ligero','IX','Árbol tecnológico'),(20257,'Sheridan','Estados Unidos','Ligero','X','Árbol tecnológico'),(22545,'Kanonenjagdpanzer','Alemania','Destructor','IX','Coleccionista'),(28689,'Rhm. Pzw.','Alemania','Ligero','X','Árbol tecnológico'),(64065,'FCM 50 t','Francia','Medio','VIII','Coleccionista');
/*!40000 ALTER TABLE `tanques` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tanques_caracteristicas`
--

DROP TABLE IF EXISTS `tanques_caracteristicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tanques_caracteristicas` (
  `tanque_id` int NOT NULL,
  `caracteristica_id` int NOT NULL,
  PRIMARY KEY (`tanque_id`,`caracteristica_id`),
  KEY `caracteristica_id` (`caracteristica_id`),
  CONSTRAINT `tanques_caracteristicas_ibfk_1` FOREIGN KEY (`tanque_id`) REFERENCES `tanques` (`id`),
  CONSTRAINT `tanques_caracteristicas_ibfk_2` FOREIGN KEY (`caracteristica_id`) REFERENCES `caracteristicas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tanques_caracteristicas`
--

LOCK TABLES `tanques_caracteristicas` WRITE;
/*!40000 ALTER TABLE `tanques_caracteristicas` DISABLE KEYS */;
INSERT INTO `tanques_caracteristicas` VALUES (10033,1),(20257,1),(22545,1),(28689,1),(64065,1),(10033,4),(22545,4),(64065,4),(10033,5),(20257,5),(28689,6),(64065,6),(10033,7),(22545,7),(22545,8),(20257,9),(28689,9),(22545,10),(28689,10),(64065,10),(22545,11),(10033,12),(64065,12),(22545,13),(28689,13),(22545,14);
/*!40000 ALTER TABLE `tanques_caracteristicas` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-02 11:40:16
