/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 10.4.17-MariaDB : Database - db_bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_bank` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `db_bank`;

/*Table structure for table `tb_integrasi` */

DROP TABLE IF EXISTS `tb_integrasi`;

CREATE TABLE `tb_integrasi` (
  `id_transaksi` int(11) NOT NULL,
  `rekening` varchar(30) DEFAULT NULL,
  `tanggal` datetime DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `status` enum('not paid','paid') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_integrasi` */

insert  into `tb_integrasi`(`id_transaksi`,`rekening`,`tanggal`,`total`,`status`) values 
(1,'401654231','2021-04-07 21:47:20',850000,'not paid'),
(2,'85412354','2021-04-07 21:47:55',8512354,'not paid'),
(3,'23213546','2021-04-07 21:49:29',2132154,'not paid'),
(4,'21546897','2021-04-07 21:52:48',798564213,'not paid'),
(5,'5644321','2021-04-07 21:56:36',78984654,'not paid'),
(6,'7987654','2021-04-07 21:59:09',7894651,'not paid'),
(7,'4562132','2021-04-07 22:09:02',4555110,'not paid'),
(8,'789456','2021-04-07 22:20:03',4564654,'not paid'),
(9,'456456456','2021-04-07 22:22:09',789754654,'not paid'),
(10,'312645','2021-04-07 22:23:16',132645,'not paid'),
(11,'321645','2021-04-07 22:25:04',879645123,'not paid'),
(12,'321465','2021-04-07 22:25:24',654132,'not paid'),
(13,'321654879','2021-04-07 22:27:04',645987132,'not paid'),
(14,'231645789','2021-04-07 22:27:24',654132546,'not paid'),
(15,'231564','2021-04-07 22:29:20',65487132,'not paid'),
(16,'111111111','2021-04-07 22:32:03',645132,'not paid');

/*Table structure for table `tb_transaksi` */

DROP TABLE IF EXISTS `tb_transaksi`;

CREATE TABLE `tb_transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `rekening` varchar(30) DEFAULT NULL,
  `tanggal` datetime DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `status` enum('not paid','paid') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_transaksi` */

insert  into `tb_transaksi`(`id_transaksi`,`rekening`,`tanggal`,`total`,`status`) values 
(1,'401654231','2021-04-07 21:47:20',850000,'not paid'),
(2,'85412354','2021-04-07 21:47:55',8512354,'not paid'),
(3,'23213546','2021-04-07 21:49:29',2132154,'not paid'),
(4,'21546897','2021-04-07 21:52:48',798564213,'not paid'),
(5,'5644321','2021-04-07 21:56:36',78984654,'not paid'),
(6,'7987654','2021-04-07 21:59:09',7894651,'not paid'),
(7,'4562132','2021-04-07 22:09:02',4555110,'not paid'),
(8,'789456','2021-04-07 22:20:03',4564654,'not paid'),
(9,'456456456','2021-04-07 22:22:09',789754654,'not paid'),
(10,'312645','2021-04-07 22:23:16',132645,'not paid'),
(11,'321645','2021-04-07 22:25:04',879645123,'not paid'),
(12,'321465','2021-04-07 22:25:24',654132,'not paid'),
(13,'321654879','2021-04-07 22:27:04',645987132,'not paid'),
(14,'231645789','2021-04-07 22:27:24',654132546,'not paid'),
(15,'231564','2021-04-07 22:29:20',65487132,'not paid'),
(16,'111111111','2021-04-07 22:32:03',645132,'not paid');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
