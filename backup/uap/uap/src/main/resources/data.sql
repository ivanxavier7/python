DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS contact_messages;

CREATE TABLE `accounts` (
   `account_number` int NOT NULL,
   `email` varchar(100) NOT NULL,
  `account_type` varchar(100) NOT NULL,
  `branch_address` varchar(200) NOT NULL,
  `create_dt` date DEFAULT NULL,
  PRIMARY KEY (`account_number`)
);

INSERT INTO `accounts` (`account_number`,`email`, `account_type`, `branch_address`, `create_dt`)
 VALUES (186576453,'sio_student@ua.pt', 'Manager', 'Avenida João Jacinto de Magalhães, DETI-UA', CURDATE());
 
CREATE TABLE `books` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(26) NOT NULL,
  `description` varchar(100) NOT NULL,
  `author` varchar(26) NOT NULL,
  `price` int NOT NULL,
  `email` varchar(100)  NOT NULL,
  PRIMARY KEY (`book_id`)
);

INSERT INTO `books` VALUES (1,'Book1','This is a simple description for the book','Author1',50,'sio_student@ua.pt'),(2,'Book2','This is a simple description for the book','Author2',50,'sio_student@ua.pt'),(3,'Book3','This is a simple description for the book','Author3',50,'sio_student@ua.pt');

CREATE TABLE `contact_messages` (
  `contact_id` varchar(50) NOT NULL,
  `contact_name` varchar(50) NOT NULL,
  `contact_email` varchar(100) NOT NULL,
  `subject` varchar(500) NOT NULL,
  `message` varchar(2000) NOT NULL,
  `create_dt` date DEFAULT NULL,
  PRIMARY KEY (`contact_id`)
);
