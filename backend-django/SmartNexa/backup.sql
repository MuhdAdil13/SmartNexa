-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: smartnexa
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add customer',7,'add_customer'),(26,'Can change customer',7,'change_customer'),(27,'Can delete customer',7,'delete_customer'),(28,'Can view customer',7,'view_customer'),(29,'Can add admin',8,'add_admin'),(30,'Can change admin',8,'change_admin'),(31,'Can delete admin',8,'delete_admin'),(32,'Can view admin',8,'view_admin'),(33,'Can add inventory',9,'add_inventory'),(34,'Can change inventory',9,'change_inventory'),(35,'Can delete inventory',9,'delete_inventory'),(36,'Can view inventory',9,'view_inventory'),(37,'Can add products',10,'add_products'),(38,'Can change products',10,'change_products'),(39,'Can delete products',10,'delete_products'),(40,'Can view products',10,'view_products'),(41,'Can add seller',11,'add_seller'),(42,'Can change seller',11,'change_seller'),(43,'Can delete seller',11,'delete_seller'),(44,'Can view seller',11,'view_seller'),(45,'Can add transaction',12,'add_transaction'),(46,'Can change transaction',12,'change_transaction'),(47,'Can delete transaction',12,'delete_transaction'),(48,'Can view transaction',12,'view_transaction'),(49,'Can add order',13,'add_order'),(50,'Can change order',13,'change_order'),(51,'Can delete order',13,'delete_order'),(52,'Can view order',13,'view_order'),(53,'Can add order_details',14,'add_order_details'),(54,'Can change order_details',14,'change_order_details'),(55,'Can delete order_details',14,'delete_order_details'),(56,'Can view order_details',14,'view_order_details'),(57,'Can add cart',15,'add_cart'),(58,'Can change cart',15,'change_cart'),(59,'Can delete cart',15,'delete_cart'),(60,'Can view cart',15,'view_cart');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_admin`
--

DROP TABLE IF EXISTS `base_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_admin` (
  `admin_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_admin`
--

LOCK TABLES `base_admin` WRITE;
/*!40000 ALTER TABLE `base_admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_cart`
--

DROP TABLE IF EXISTS `base_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_cart` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `product_quantity` int(11) NOT NULL,
  `customer_id_id` int(11) NOT NULL,
  `product_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `base_cart_customer_id_id_product_id_id_81570514_uniq` (`customer_id_id`,`product_id_id`),
  KEY `base_cart_product_id_id_d32ee1b2_fk_base_products_product_id` (`product_id_id`),
  CONSTRAINT `base_cart_customer_id_id_bbc4c0ff_fk_base_customer_customer_id` FOREIGN KEY (`customer_id_id`) REFERENCES `base_customer` (`customer_id`),
  CONSTRAINT `base_cart_product_id_id_d32ee1b2_fk_base_products_product_id` FOREIGN KEY (`product_id_id`) REFERENCES `base_products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_cart`
--

LOCK TABLES `base_cart` WRITE;
/*!40000 ALTER TABLE `base_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_customer`
--

DROP TABLE IF EXISTS `base_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `address_1` longtext NOT NULL,
  `address_2` longtext NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_customer`
--

LOCK TABLES `base_customer` WRITE;
/*!40000 ALTER TABLE `base_customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_inventory`
--

DROP TABLE IF EXISTS `base_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_inventory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `price` decimal(7,2) NOT NULL,
  `original_price` decimal(7,2) NOT NULL,
  `stock_quantity` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_inventory`
--

LOCK TABLES `base_inventory` WRITE;
/*!40000 ALTER TABLE `base_inventory` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_order`
--

DROP TABLE IF EXISTS `base_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_date` datetime(6) NOT NULL,
  `order_status` varchar(10) NOT NULL,
  `customer_id_id` int(11) NOT NULL,
  `transaction_id_id` varchar(100) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `base_order_customer_id_id_3d3f4baf_fk_base_customer_customer_id` (`customer_id_id`),
  KEY `base_order_transaction_id_id_71b9b011_fk_base_tran` (`transaction_id_id`),
  CONSTRAINT `base_order_customer_id_id_3d3f4baf_fk_base_customer_customer_id` FOREIGN KEY (`customer_id_id`) REFERENCES `base_customer` (`customer_id`),
  CONSTRAINT `base_order_transaction_id_id_71b9b011_fk_base_tran` FOREIGN KEY (`transaction_id_id`) REFERENCES `base_transaction` (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_order`
--

LOCK TABLES `base_order` WRITE;
/*!40000 ALTER TABLE `base_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_order_details`
--

DROP TABLE IF EXISTS `base_order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_order_details` (
  `order_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_quantity` int(11) NOT NULL,
  `total_amount` decimal(7,2) NOT NULL,
  `order_id_id` int(11) NOT NULL,
  `product_id_id` int(11) NOT NULL,
  PRIMARY KEY (`order_details_id`),
  KEY `base_order_details_order_id_id_26083772_fk_base_order_order_id` (`order_id_id`),
  KEY `base_order_details_product_id_id_5ea08ae8_fk_base_prod` (`product_id_id`),
  CONSTRAINT `base_order_details_order_id_id_26083772_fk_base_order_order_id` FOREIGN KEY (`order_id_id`) REFERENCES `base_order` (`order_id`),
  CONSTRAINT `base_order_details_product_id_id_5ea08ae8_fk_base_prod` FOREIGN KEY (`product_id_id`) REFERENCES `base_products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_order_details`
--

LOCK TABLES `base_order_details` WRITE;
/*!40000 ALTER TABLE `base_order_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_order_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_products`
--

DROP TABLE IF EXISTS `base_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(255) NOT NULL,
  `slug` longtext NOT NULL,
  `categories` varchar(255) NOT NULL,
  `brand_name` varchar(100) NOT NULL,
  `images` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `short_description` longtext NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_products`
--

LOCK TABLES `base_products` WRITE;
/*!40000 ALTER TABLE `base_products` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_seller`
--

DROP TABLE IF EXISTS `base_seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_seller` (
  `seller_id` int(11) NOT NULL AUTO_INCREMENT,
  `seller_name` varchar(255) NOT NULL,
  `legal_name` varchar(255) NOT NULL,
  `contact_person` varchar(255) NOT NULL,
  `alter_mobile` varchar(14) NOT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_seller`
--

LOCK TABLES `base_seller` WRITE;
/*!40000 ALTER TABLE `base_seller` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_seller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_transaction`
--

DROP TABLE IF EXISTS `base_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_transaction` (
  `transaction_id` varchar(100) NOT NULL,
  `date` datetime(6) NOT NULL,
  `payment_method` varchar(20) NOT NULL,
  `amount` decimal(7,2) NOT NULL,
  `status` varchar(10) NOT NULL,
  `ip_address` varchar(35) NOT NULL,
  `response_code` int(11) NOT NULL,
  `response_message` varchar(100) NOT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_transaction`
--

LOCK TABLES `base_transaction` WRITE;
/*!40000 ALTER TABLE `base_transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'base','admin'),(15,'base','cart'),(7,'base','customer'),(9,'base','inventory'),(13,'base','order'),(14,'base','order_details'),(10,'base','products'),(11,'base','seller'),(12,'base','transaction'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-07-16 07:27:41.355863'),(2,'auth','0001_initial','2024-07-16 07:27:41.729284'),(3,'admin','0001_initial','2024-07-16 07:27:41.828227'),(4,'admin','0002_logentry_remove_auto_add','2024-07-16 07:27:41.832285'),(5,'admin','0003_logentry_add_action_flag_choices','2024-07-16 07:27:41.847377'),(6,'contenttypes','0002_remove_content_type_name','2024-07-16 07:27:41.911509'),(7,'auth','0002_alter_permission_name_max_length','2024-07-16 07:27:41.953137'),(8,'auth','0003_alter_user_email_max_length','2024-07-16 07:27:41.970206'),(9,'auth','0004_alter_user_username_opts','2024-07-16 07:27:41.972474'),(10,'auth','0005_alter_user_last_login_null','2024-07-16 07:27:42.020873'),(11,'auth','0006_require_contenttypes_0002','2024-07-16 07:27:42.023138'),(12,'auth','0007_alter_validators_add_error_messages','2024-07-16 07:27:42.028716'),(13,'auth','0008_alter_user_username_max_length','2024-07-16 07:27:42.048632'),(14,'auth','0009_alter_user_last_name_max_length','2024-07-16 07:27:42.062891'),(15,'auth','0010_alter_group_name_max_length','2024-07-16 07:27:42.079787'),(16,'auth','0011_update_proxy_permissions','2024-07-16 07:27:42.079787'),(17,'auth','0012_alter_user_first_name_max_length','2024-07-16 07:27:42.100298'),(18,'base','0001_initial','2024-07-16 07:27:42.109361'),(19,'base','0002_admin_inventory_products_seller_transaction_and_more','2024-07-16 07:27:42.448428'),(20,'base','0003_remove_products_description_and_more','2024-07-16 07:27:42.511724'),(21,'base','0004_products_description_products_short_description','2024-07-16 07:27:42.544929'),(22,'sessions','0001_initial','2024-07-16 07:27:42.573589');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-16 13:07:09
