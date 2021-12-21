CREATE DATABASE  IF NOT EXISTS `uap`;
USE `uap`;

CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile_number` varchar(20) NOT NULL,
  `pwd` varchar(500) NOT NULL,
  `role` varchar(100) NOT NULL,
  `create_dt` date DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
);

INSERT INTO `customer` VALUES (1,'Happy','happy@example.com','9876548337','$2y$12$oRRbkNfwuR8ug4MlzH5FOeui.//1mkd.RsOAJMbykTSupVy.x/vb2','admin','2021-12-20');

CREATE TABLE `accounts` (
  `customer_id` int NOT NULL,
  `account_number` int NOT NULL,
  `account_type` varchar(100) NOT NULL,
  `branch_address` varchar(200) NOT NULL,
  `create_dt` date DEFAULT NULL,
  PRIMARY KEY (`account_number`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE
);

INSERT INTO `accounts` VALUES (1,2147483647,'Savings','123 Main Street, New York','2021-12-20');

CREATE TABLE `authorities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `authorities_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)
);

INSERT INTO `authorities` VALUES (1,1,'ROLE_USER'),(2,1,'ROLE_ADMIN'),(3,1,'ROLE_ROOT');

CREATE TABLE `books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `name` varchar(26) NOT NULL,
  `description` varchar(100) NOT NULL,
  `author` varchar(26) NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `book_customer_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE
);

INSERT INTO `books` VALUES (1,1,'book1','this is a book','author1',50),(2,1,'book3','this is a book','author2',50),(3,1,'book3','this is a book','author3',50);

CREATE TABLE `cards` (
  `card_id` int NOT NULL AUTO_INCREMENT,
  `card_number` varchar(100) NOT NULL,
  `customer_id` int NOT NULL,
  `card_type` varchar(100) NOT NULL,
  `total_limit` int NOT NULL,
  `amount_used` int NOT NULL,
  `available_amount` int NOT NULL,
  `create_dt` date DEFAULT NULL,
  PRIMARY KEY (`card_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `card_customer_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE
);

INSERT INTO `cards` VALUES (1,'4565XXXX4656',1,'Credit',10000,500,9500,'2021-12-20'),(2,'3455XXXX8673',1,'Credit',7500,600,6900,'2021-12-20'),(3,'2359XXXX9346',1,'Credit',20000,4000,16000,'2021-12-20');

CREATE TABLE `contact_messages` (
  `contact_id` varchar(50) NOT NULL,
  `contact_name` varchar(50) NOT NULL,
  `contact_email` varchar(100) NOT NULL,
  `subject` varchar(500) NOT NULL,
  `message` varchar(2000) NOT NULL,
  `create_dt` date DEFAULT NULL,
  PRIMARY KEY (`contact_id`)
);

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `enabled` int NOT NULL,
  PRIMARY KEY (`id`)
);
INSERT INTO `users` VALUES (1,'happy','12345',1);

CREATE TABLE account_transactions (
  transaction_id varchar(200) NOT NULL,
  account_number int NOT NULL,
  customer_id int NOT NULL,
  transaction_dt date NOT NULL,
  transaction_summary varchar(200) NOT NULL,
  transaction_type varchar(100) NOT NULL,
  transaction_amt int NOT NULL,
  closing_balance int NOT NULL,
  create_dt date DEFAULT NULL,
  PRIMARY KEY (transaction_id),
  KEY customer_id (customer_id),
  KEY account_number (account_number),
  CONSTRAINT accounts_ibfk_2 FOREIGN KEY (account_number) REFERENCES accounts (account_number) ON DELETE CASCADE,
  CONSTRAINT acct_user_ibfk_1 FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ON DELETE CASCADE
);

INSERT INTO account_transactions (transaction_id, account_number, customer_id, transaction_dt, transaction_summary, transaction_type,transaction_amt,
closing_balance, create_dt)  VALUES (UUID(), 2147483647, 1, CURDATE()-7, 'Coffee Shop', 'Withdrawal', 30,34500,CURDATE()-7);

INSERT INTO account_transactions (transaction_id, account_number, customer_id, transaction_dt, transaction_summary, transaction_type,transaction_amt,
closing_balance, create_dt)  VALUES (UUID(), 2147483647, 1, CURDATE()-6, 'Uber', 'Withdrawal', 100,34400,CURDATE()-6);

INSERT INTO account_transactions (transaction_id, account_number, customer_id, transaction_dt, transaction_summary, transaction_type,transaction_amt,
closing_balance, create_dt)  VALUES (UUID(), 2147483647, 1, CURDATE()-5, 'Self Deposit', 'Deposit', 500,34900,CURDATE()-5);

INSERT INTO account_transactions (transaction_id, account_number, customer_id, transaction_dt, transaction_summary, transaction_type,transaction_amt,
closing_balance, create_dt)  VALUES (UUID(), 2147483647, 1, CURDATE()-4, 'Ebay', 'Withdrawal', 600,34300,CURDATE()-4);

INSERT INTO account_transactions (transaction_id, account_number, customer_id, transaction_dt, transaction_summary, transaction_type,transaction_amt,
closing_balance, create_dt)  VALUES (UUID(), 2147483647, 1, CURDATE()-2, 'OnlineTransfer', 'Deposit', 700,35000,CURDATE()-2);

INSERT INTO account_transactions (transaction_id, account_number, customer_id, transaction_dt, transaction_summary, transaction_type,transaction_amt,
closing_balance, create_dt)  VALUES (UUID(), 2147483647, 1, CURDATE()-1, 'Amazon.com', 'Withdrawal', 100,34900,CURDATE()-1);

