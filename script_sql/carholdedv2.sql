-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: carholdedv2
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `Alta`
--

DROP TABLE IF EXISTS `Alta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Alta` (
  `CodigoVenta` int NOT NULL AUTO_INCREMENT,
  `Fecha` date NOT NULL,
  `Importe` float NOT NULL,
  `CodigoUsuario` int DEFAULT NULL,
  `Matricula` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`CodigoVenta`),
  KEY `fk_vehiculo2` (`Matricula`),
  KEY `fk_usuario2` (`CodigoUsuario`),
  CONSTRAINT `fk_usuario2` FOREIGN KEY (`CodigoUsuario`) REFERENCES `Usuarios` (`CodigoUsuario`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_vehiculo2` FOREIGN KEY (`Matricula`) REFERENCES `Vehiculos` (`Matricula`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Alta`
--

LOCK TABLES `Alta` WRITE;
/*!40000 ALTER TABLE `Alta` DISABLE KEYS */;
INSERT INTO `Alta` VALUES (2,'2023-04-30',25400,3,'AGSHDJKISA'),(3,'2023-04-29',115400,5,'HJSKALSOQ'),(4,'2023-04-28',54600,5,'1234567890'),(5,'2023-05-02',19500,3,'12345JFKGL'),(6,'2023-05-02',27500,3,'JAHSJDKSLO'),(7,'2023-05-03',123450,3,'1234567891'),(8,'2023-05-03',18765,3,'12345KDJHD'),(9,'2023-05-03',67908,3,'KAJDOELSPA'),(10,'2023-05-03',12345,3,'AJDKFLDPSA'),(11,'2023-05-03',24343,3,'AKSJDORITN'),(12,'2023-05-03',67543,3,'JAHSLOSKAM'),(13,'2023-05-03',32455,3,'SHDJFKGLPO'),(14,'2023-05-03',23465,3,'KAJSKDOPRT'),(15,'2023-05-05',123450,3,'12345JHAOS'),(16,'2023-05-10',12300,10,'SGDHSJAKOQ'),(17,'2023-05-11',23455,3,'HSJAKSOELA'),(18,'2023-05-15',12344,5,'ASDFGHJKER'),(19,'2023-05-15',108709,3,'HSJAKSLAOS'),(20,'2023-05-15',134558,3,'JSKALSONAI'),(21,'2023-05-15',29879,NULL,'HSJAUEISO1'),(22,'2023-05-22',127655,NULL,'ASDFER2345'),(23,'2023-05-22',27866,NULL,'HAJSIEKAOS'),(24,'2023-05-24',23455,12,'123ASDERTY'),(25,'2023-05-24',47866,12,'342ABHSJKO'),(26,'2023-05-24',12344,12,'OEKDIAKSOP'),(27,'2023-05-24',23477,12,'AKSOELSAOO'),(28,'2023-05-24',54899,12,'JDKSLAOSJE'),(29,'2023-05-24',102566,12,'8473839303'),(30,'2023-05-24',156788,12,'SJDHGTPKSA');
/*!40000 ALTER TABLE `Alta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Compra`
--

DROP TABLE IF EXISTS `Compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Compra` (
  `CodigoCompra` int NOT NULL AUTO_INCREMENT,
  `Fecha` date NOT NULL,
  `Importe` float NOT NULL,
  `CodigoUsuario` int DEFAULT NULL,
  `Matricula` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`CodigoCompra`),
  KEY `fk_vehiculo` (`Matricula`),
  KEY `fk_usuario` (`CodigoUsuario`),
  CONSTRAINT `fk_usuario` FOREIGN KEY (`CodigoUsuario`) REFERENCES `Usuarios` (`CodigoUsuario`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_vehiculo` FOREIGN KEY (`Matricula`) REFERENCES `Vehiculos` (`Matricula`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Compra`
--

LOCK TABLES `Compra` WRITE;
/*!40000 ALTER TABLE `Compra` DISABLE KEYS */;
INSERT INTO `Compra` VALUES (2,'2023-04-30',25400,5,'AGSHDJKISA'),(4,'2023-04-29',115400,3,'HJSKALSOQ'),(5,'2023-04-28',54600,3,'1234567890'),(6,'2023-05-03',115999,3,'HJSKALSOQ'),(7,'2023-05-03',54600,3,'1234567890'),(8,'2023-05-03',54600,3,'1234567890'),(9,'2023-05-03',123450,5,'1234567891'),(10,'2023-05-03',27500,5,'JAHSJDKSLO'),(11,'2023-05-03',23500,5,'AGSHDJKISA'),(12,'2023-05-03',19500,5,'12345JFKGL'),(13,'2023-05-03',67543,5,'JAHSLOSKAM'),(14,'2023-05-03',32455,5,'SHDJFKGLPO'),(15,'2023-05-03',67908,5,'KAJDOELSPA'),(16,'2023-05-03',12345,5,'AJDKFLDPSA'),(17,'2023-05-05',123450,5,'12345JHAOS'),(18,'2023-05-10',24343,10,'AKSJDORITN'),(19,'2023-05-11',12300,3,'SGDHSJAKOQ'),(20,'2023-05-11',23455,5,'HSJAKSOELA'),(21,'2023-05-15',23465,NULL,'KAJSKDOPRT'),(22,'2023-05-15',18765,NULL,'12345KDJHD'),(23,'2023-05-15',12344,NULL,'ASDFGHJKER'),(24,'2023-05-15',134558,NULL,'JSKALSONAI'),(25,'2023-05-15',29879,3,'HSJAUEISO1'),(26,'2023-05-22',127655,3,'ASDFER2345'),(27,'2023-05-24',108709,12,'HSJAKSLAOS');
/*!40000 ALTER TABLE `Compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Marcas`
--

DROP TABLE IF EXISTS `Marcas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Marcas` (
  `CodigoMarca` int NOT NULL AUTO_INCREMENT,
  `NombreMarca` varchar(70) NOT NULL,
  PRIMARY KEY (`CodigoMarca`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Marcas`
--

LOCK TABLES `Marcas` WRITE;
/*!40000 ALTER TABLE `Marcas` DISABLE KEYS */;
INSERT INTO `Marcas` VALUES (1,'Volswagen'),(2,'Audi'),(3,'Mercedes'),(4,'Renault'),(5,'Porche'),(6,'Seat'),(7,'Chevrolet'),(8,'BMW'),(9,'Nissan'),(10,'Citroen');
/*!40000 ALTER TABLE `Marcas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuarios`
--

DROP TABLE IF EXISTS `Usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuarios` (
  `CodigoUsuario` int NOT NULL AUTO_INCREMENT,
  `CorreoElectronico` varchar(70) NOT NULL,
  `Nombre` varchar(70) NOT NULL,
  `PrimerApellido` varchar(70) NOT NULL,
  `SegundoApellido` varchar(70) DEFAULT NULL,
  `CantidadGastada` float NOT NULL,
  `CantidadVendida` float NOT NULL,
  `Contraseña` varchar(15) NOT NULL,
  PRIMARY KEY (`CodigoUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuarios`
--

LOCK TABLES `Usuarios` WRITE;
/*!40000 ALTER TABLE `Usuarios` DISABLE KEYS */;
INSERT INTO `Usuarios` VALUES (3,'alicia@gmail.com','Alicia','Rovira','Escudero',395033,830946,'25852585'),(5,'edu@gmail.com','Eduardo','Gil','',521106,237543,'25852585'),(8,'rafa@gmail.com','Rafa','Rodriguez','',0,0,'25852585'),(9,'vashori@gmail.com','Vicente','Sahori','',0,0,'25852585'),(10,'vsahori@gmail.com','Vicente','Sahori','',24343,12300,'25852585'),(12,'ejemplo@gmail.com','Ejemplo','Ejemplo','',108709,0,'12345'),(13,'marcos@gmail.com','Marcos','Rovira','Escudero',0,0,'25852585');
/*!40000 ALTER TABLE `Usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Vehiculos`
--

DROP TABLE IF EXISTS `Vehiculos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Vehiculos` (
  `Matricula` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Modelo` varchar(70) NOT NULL,
  `Color` varchar(10) NOT NULL,
  `Precio` float NOT NULL,
  `CodigoMarca` int DEFAULT NULL,
  `Vendido` tinyint(1) NOT NULL,
  PRIMARY KEY (`Matricula`),
  KEY `fk_marcas` (`CodigoMarca`),
  CONSTRAINT `fk_marcas` FOREIGN KEY (`CodigoMarca`) REFERENCES `Marcas` (`CodigoMarca`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vehiculos`
--

LOCK TABLES `Vehiculos` WRITE;
/*!40000 ALTER TABLE `Vehiculos` DISABLE KEYS */;
INSERT INTO `Vehiculos` VALUES ('1234567890','Audi a4','Amarillo',54600,2,1),('1234567891','Taikan','Negro',123450,5,1),('12345JFKGL','Volswagen Golf','Blanco',19500,1,1),('12345JHAOS','Benz','Blanco',123450,3,1),('12345KDJHD','A6','Negro',18765,2,1),('123ASDERTY','Clio','Blanco',23455,4,0),('342ABHSJKO','Megane','Negro',47866,4,0),('8473839303','Benz-07','Blanco',102566,3,0),('AGSHDJKISA','Volswagen Polo','Amarillo',23500,1,1),('AJDKFLDPSA','Golf','Blanco',12345,1,1),('AKSJDORITN','q5','Marrón',24343,2,1),('AKSOELSAOO','León','Amarillo',23477,6,0),('ASDFER2345','Class g','Negro',127655,5,1),('ASDFGHJKER','C4','Blanco',12344,10,1),('HAJSIEKAOS','Golf','Negro',27866,1,0),('HJSKALSOQ','Mercedes Benz','Blanco',115999,3,1),('HSJAKSLAOS','Benz-06','Blanco',108709,3,1),('HSJAKSOELA','Polo','Azul',23455,1,1),('HSJAUEISO1','León','Negro',29879,6,1),('JAHSJDKSLO','Qasqai','Verde',27500,9,1),('JAHSLOSKAM','Cayanne','Blanco',67543,5,1),('JDKSLAOSJE','C5','Blanco',54899,10,0),('JSKALSONAI','GTR Skyline','Blanco',134558,9,1),('KAJDOELSPA','León','Blanco',67908,6,1),('KAJSKDOPRT','Benz-05','Azul',23465,3,1),('OEKDIAKSOP','M5','Azul',12344,8,0),('SGDHSJAKOQ','A5','Blanco',12300,2,1),('SHDJFKGLPO','Daewoo','Rojo',32455,7,1),('SJDHGTPKSA','AMG-GT','Negro',156788,3,0);
/*!40000 ALTER TABLE `Vehiculos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'carholdedv2'
--

--
-- Dumping routines for database 'carholdedv2'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-25 20:34:17
