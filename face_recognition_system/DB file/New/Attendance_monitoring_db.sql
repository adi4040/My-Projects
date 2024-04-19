-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: face_recognizer
-- ------------------------------------------------------
-- Server version	8.0.35

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

--
-- Table structure for table `appended_data`
--

DROP TABLE IF EXISTS `appended_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appended_data` (
  `Name` varchar(45) DEFAULT NULL,
  `RollNo` varchar(45) DEFAULT NULL,
  `Dep` varchar(45) DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Time(In)` varchar(45) DEFAULT NULL,
  `Time(Out)` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appended_data`
--

LOCK TABLES `appended_data` WRITE;
/*!40000 ALTER TABLE `appended_data` DISABLE KEYS */;
INSERT INTO `appended_data` VALUES ('Aditya','22','Computer','30/03/2024','11:14:23','19:13:11'),('Sejal','39','Computer','','',''),('Anuj','13','IT','','',''),('Arjun','1','Civil','','',''),('Susheel','16','Computer','','',''),('Kapil','17','Computer','21/03/2024','12:35:13',''),('Archit','10','IT','','',''),('Aditya','22','Computer','30/03/2024','11:14:23','19:13:11'),('Sejal','39','Computer','','',''),('Anuj','13','IT','','',''),('Arjun','1','Civil','','',''),('Susheel','16','Computer','','',''),('Kapil','17','Computer','21/03/2024','12:35:13',''),('Archit','10','IT','','','');
/*!40000 ALTER TABLE `appended_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendancetb`
--

DROP TABLE IF EXISTS `attendancetb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendancetb` (
  `ID` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Roll No` varchar(45) DEFAULT NULL,
  `Dep` varchar(45) DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Status (In)` varchar(45) DEFAULT NULL,
  `Status (out)` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendancetb`
--

LOCK TABLES `attendancetb` WRITE;
/*!40000 ALTER TABLE `attendancetb` DISABLE KEYS */;
INSERT INTO `attendancetb` VALUES ('1','Aditya','22','Computer','07/04/2024','17:57:50','17:59:52'),('2','Sejal','39','Computer','','',''),('3','Anuj','13','IT','','',''),('4','Arjun','1','Civil','','',''),('5','Susheel','16','Computer','','',''),('6','Kapil','17','Computer','21/03/2024','',''),('7','Archit','10','IT','04/04/2024','','');
/*!40000 ALTER TABLE `attendancetb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Dep` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Student_id` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Division` varchar(45) DEFAULT NULL,
  `Roll` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('Computer','TY','2022-23','1','Aditya','2','51','adi@gmail.com','8975523983','Yes'),('Computer','SY','2021-22','10','name','2','10','sachin@gmail.com','97875454','Yes'),('Computer','SY','2021-22','11','Hardik','2','10','hardik@gmail.com','978754548','Yes'),('Computer','TY','2021-22','2','Sejal','2','39','sejal@gmail.com','78454878545','Yes'),('IT','TY','2022-23','3','Anuj','2','13','anuj@gmail.com','8754548754','Yes'),('Civil','TY','2021-22','4','Arjun','3','1','arjun@gmail.com','4548712121','Yes'),('Computer','TY','2021-22','5','Susheel','2','16','susheel@gmail.com','123423312','Yes'),('Computer','TY','2021-22','6','Kapil','2','17','kapil@gmail.com','123423311','Yes'),('IT','TY','2022-23','7','Archit','2','10','archit@gmail.com','123123',''),('Computer','SY','2021-22','9','Sachin','2','10','sachin@gmail.com','978754548','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-15  9:22:51
