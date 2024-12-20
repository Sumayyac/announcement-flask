/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.1.32-community : Database - announcement
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`announcement` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `announcement`;

/*Table structure for table `announce` */

DROP TABLE IF EXISTS `announce`;

CREATE TABLE `announce` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `date` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `file` varchar(50) NOT NULL,
  `status` varchar(10) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `announce` */

insert  into `announce`(`id`,`title`,`date`,`department`,`file`,`status`,`userid`) values 
(1,'arts','11-12-2024','cs','mm.jpg','rejected',NULL),
(2,'sports','13-12-2024','all','nn.jpg','rejected',NULL),
(3,'sports','11:00','all','hfhh.jpg','rejected',29),
(4,'college day','10:00','all','fgd.mp3','pending',31),
(5,'scholar','3:00','all','fdfs.jpg','pending',32);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `id` int(11) NOT NULL,
  `content` text NOT NULL,
  `date` varchar(50) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`id`,`feedback`,`date`) values 
(3,'sdfghj','2024-12-15'),
(4,'sdfghj','2024-12-15'),
(5,'rtyu','2024-12-15');

/*Table structure for table `hod` */

DROP TABLE IF EXISTS `hod`;

CREATE TABLE `hod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `hod` */

insert  into `hod`(`id`,`name`,`department`,`qualification`,`email`,`phone`,`login_id`) values 
(5,'farsana','cs','bsc','hjj@gmail.com','1567654345',30),
(6,'jishna','cs','bca','hjj@gmail.com','987654323',33),
(7,'sumayya','cs','bca','hjj@gmail.com','8765432',34);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `usertype` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(6,'farsana','123','HOD'),
(11,'jishna','123','Teacher'),
(12,'nasrin','789','Staff'),
(13,'nasrin','345','UNION'),
(20,'hhj','123','UNION'),
(21,'adhilappp','23','REP'),
(22,'farsana','987','HOD'),
(23,'fidh','233','Teacher'),
(24,'hod','123','Teacher'),
(25,'HIOO','987','HOD'),
(26,'admin','hj','REP'),
(27,'farsana','jhgfd','UNION'),
(28,'hgfds','jgfdsa','Staff'),
(29,'jishna','lkjhg','REP'),
(30,'hod','433','HOD'),
(31,'fidha','567','REP'),
(32,'adhila','234','REP'),
(33,'jishna','123','HOD'),
(34,'jishna','543','HOD');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(150) NOT NULL,
  `announceid` varchar(150) NOT NULL,
  `time` varchar(50) NOT NULL,
  `status` tinyint(4) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

/*Table structure for table `rep` */

DROP TABLE IF EXISTS `rep`;

CREATE TABLE `rep` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `semester` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `rep` */

insert  into `rep`(`id`,`name`,`department`,`semester`,`email`,`phone`,`login_id`) values 
(3,'adhilap','cs','6','hjj@gmail.com','09876543',29),
(4,'fidha','cs','5','hjj@gmail.com','765432',31),
(5,'adhila','cs','4','hjj@gmail.com','234567',32);

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`id`,`name`,`email`,`phone`,`login_id`) values 
(1,'nasrin','hjj@gmail.com','0987654321',12);

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `teacher` */

insert  into `teacher`(`id`,`name`,`department`,`qualification`,`email`,`phone`,`login_id`) values 
(3,'fidha','cs','bsc ','hjj@gmail.com','9876456788',23),
(4,'fidha','cs','bsc ','hjj@gmail.com','9876456788',23),
(5,'shshnasulfi','cs','bsc ','hjj@gmail.com','9876545678',24),
(6,'shshnasulfi','cs','bsc ','hjj@gmail.com','9876545678',24);

/*Table structure for table `time` */

DROP TABLE IF EXISTS `time`;

CREATE TABLE `time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `time` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `time` */

/*Table structure for table `union` */

DROP TABLE IF EXISTS `union`;

CREATE TABLE `union` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `semester` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `union` */

insert  into `union`(`id`,`name`,`department`,`semester`,`email`,`phone`,`login_id`) values 
(1,'jishnaaa','cs','6','hjj@gmail.com','8798767656',20);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
