/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 8.0.23 : Database - db_toko2
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_toko2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `db_toko2`;

/*Table structure for table `tb_integrasi` */

DROP TABLE IF EXISTS `tb_integrasi`;

CREATE TABLE `tb_integrasi` (
  `id_transaksi` int NOT NULL,
  `rekening` varchar(30) DEFAULT NULL,
  `tanggal` datetime DEFAULT NULL,
  `total` int DEFAULT NULL,
  `status` enum('not paid','paid') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `tb_integrasi` */

insert  into `tb_integrasi`(`id_transaksi`,`rekening`,`tanggal`,`total`,`status`) values 
(2,'222222222','2021-04-12 10:43:22',111111111,'not paid'),
(4,'22222222','2021-04-12 10:52:15',222222222,'paid');

/*Table structure for table `tb_transaksi` */

DROP TABLE IF EXISTS `tb_transaksi`;

CREATE TABLE `tb_transaksi` (
  `id_transaksi` int NOT NULL,
  `rekening` varchar(30) DEFAULT NULL,
  `tanggal` datetime DEFAULT NULL,
  `total` int DEFAULT NULL,
  `status` enum('not paid','paid') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `tb_transaksi` */

insert  into `tb_transaksi`(`id_transaksi`,`rekening`,`tanggal`,`total`,`status`) values 
(2,'222222222','2021-04-12 10:43:22',111111111,'not paid'),
(4,'22222222','2021-04-12 10:52:15',222222222,'paid');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
