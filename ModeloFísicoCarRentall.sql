-- -----------------------------------------------------
-- Drop Schema car_rental
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS car_rental;

-- -----------------------------------------------------
-- Create Schema car_rental
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS car_rental;
USE car_rental ;

-- -----------------------------------------------------
-- Table car_rental.discount
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.discount ;

CREATE TABLE IF NOT EXISTS car_rental.discount (
  id_discount TINYINT(2) NOT NULL AUTO_INCREMENT,
  description VARCHAR(256) NOT NULL,
  current_value DECIMAL(6,2) NOT NULL,
  PRIMARY KEY (id_discount)
);


-- -----------------------------------------------------
-- Table car_rental.person
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.person ;

CREATE TABLE IF NOT EXISTS car_rental.person (
  id_person INT NOT NULL AUTO_INCREMENT,
  cpf CHAR(11) NOT NULL,
  name VARCHAR(256) NOT NULL,
  birth_date DATE NOT NULL,
  PRIMARY KEY (id_person),
  UNIQUE cpf (cpf) VISIBLE
);


-- -----------------------------------------------------
-- Table car_rental.employee
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.employee ;

CREATE TABLE IF NOT EXISTS car_rental.employee (
  id_employee INT NOT NULL,
  salary DECIMAL(8,2) NOT NULL,
  comission DECIMAL(3,2) NULL,
  PRIMARY KEY (id_employee),
  FOREIGN KEY (id_employee) REFERENCES car_rental.person (id_person)
);


-- -----------------------------------------------------
-- Table car_rental.payment
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.payment ;

CREATE TABLE IF NOT EXISTS car_rental.payment (
  id_payment INT NOT NULL AUTO_INCREMENT,
  payment_datetime DATETIME NOT NULL,
  total_value DECIMAL(8,2) UNSIGNED NOT NULL,
  reference_month TINYINT(2) ZEROFILL NOT NULL,
  id_employee INT NOT NULL,
  PRIMARY KEY (id_payment),
  FOREIGN KEY (id_employee) REFERENCES car_rental.employee (id_employee)
);


-- -----------------------------------------------------
-- Table car_rental.client
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.client ;

CREATE TABLE IF NOT EXISTS car_rental.client (
  id_client INT NOT NULL,
  cnh CHAR(11) NOT NULL,
  UNIQUE (cnh),
  PRIMARY KEY (id_client),
  FOREIGN KEY (id_client) REFERENCES car_rental.person (id_person)
);


-- -----------------------------------------------------
-- Table car_rental.billing
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.billing ;

CREATE TABLE IF NOT EXISTS car_rental.billing (
  id_billing INT NOT NULL AUTO_INCREMENT,
  value DECIMAL(6,2) UNSIGNED NOT NULL,
  billing_datetime DATETIME NOT NULL,
  id_employee INT NOT NULL,
  PRIMARY KEY (id_billing),
  FOREIGN KEY (id_employee) REFERENCES car_rental.employee (id_employee)
);


-- -----------------------------------------------------
-- Table car_rental.rent
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.rent ;

CREATE TABLE IF NOT EXISTS car_rental.rent (
  id_rent INT NOT NULL AUTO_INCREMENT,
  reservation_date DATETIME NOT NULL,
  start_datetime DATETIME NOT NULL,
  end_datetime DATETIME NOT NULL,
  value DECIMAL(6,2) NOT NULL,
  id_billing INT NULL,
  id_client INT NOT NULL,
  id_employee INT NOT NULL,
  PRIMARY KEY (id_rent),
  FOREIGN KEY (id_billing) REFERENCES car_rental.billing (id_billing),
  FOREIGN KEY (id_client) REFERENCES car_rental.client (id_client),
  FOREIGN KEY (id_employee) REFERENCES car_rental.employee (id_employee)
);


-- -----------------------------------------------------
-- Table car_rental.payment_discounts
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.payment_discounts ;

CREATE TABLE IF NOT EXISTS car_rental.payment_discounts (
  id_payment INT NOT NULL,
  id_discount TINYINT(2) NOT NULL,
  discount_value DECIMAL(6,2) NOT NULL,
  PRIMARY KEY (id_payment, id_discount),
  FOREIGN KEY (id_payment) REFERENCES car_rental.payment (id_payment),
  FOREIGN KEY (id_discount) REFERENCES car_rental.discount (id_discount)
);


-- -----------------------------------------------------
-- Table car_rental.email
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.email ;

CREATE TABLE IF NOT EXISTS car_rental.email (
  email VARCHAR(100) NOT NULL,
  id_person INT NOT NULL,
  FOREIGN KEY (id_person) REFERENCES car_rental.person (id_person)
);


-- -----------------------------------------------------
-- Table car_rental.phone
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.phone ;

CREATE TABLE IF NOT EXISTS car_rental.phone (
  country_code SMALLINT(3) NOT NULL,
  ddd SMALLINT(3) NOT NULL,
  number BIGINT(12) NOT NULL,
  id_person INT NOT NULL,
  FOREIGN KEY (id_person) REFERENCES car_rental.person (id_person)
);


-- -----------------------------------------------------
-- Table car_rental.ticket
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.ticket ;

CREATE TABLE IF NOT EXISTS car_rental.ticket (
  id_ticket INT NOT NULL AUTO_INCREMENT,
  description VARCHAR(256) NOT NULL,
  current_value DECIMAL(6,2) UNSIGNED NOT NULL,
  PRIMARY KEY (id_ticket)
);


-- -----------------------------------------------------
-- Table car_rental.rent_tickets
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.rent_tickets ;

CREATE TABLE IF NOT EXISTS car_rental.rent_tickets (
  id_ticket INT NOT NULL,
  id_rent INT NOT NULL,
  ticket_value DECIMAL(6,2) NOT NULL,
  PRIMARY KEY (id_ticket, id_rent),
  FOREIGN KEY (id_ticket) REFERENCES car_rental.ticket (id_ticket),
  FOREIGN KEY (id_rent) REFERENCES car_rental.rent (id_rent)
);


-- -----------------------------------------------------
-- Table car_rental.car
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.car ;

CREATE TABLE IF NOT EXISTS car_rental.car (
  id_car INT NOT NULL AUTO_INCREMENT,
  current_value DECIMAL(6,2) UNSIGNED NOT NULL,
  capacity TINYINT(1) UNSIGNED NOT NULL,
  category VARCHAR(45) NOT NULL,
  chassi CHAR(17) NOT NULL,
  cor VARCHAR(20) NOT NULL,
  model_year YEAR NOT NULL,
  model VARCHAR(30) NOT NULL,
  brand VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_car)
);


-- -----------------------------------------------------
-- Table car_rental.rent_cars
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.rent_cars ;

CREATE TABLE IF NOT EXISTS car_rental.rent_cars (
  id_car INT NOT NULL,
  id_rent INT NOT NULL,
  car_value DECIMAL(6,2) UNSIGNED NOT NULL,
  FOREIGN KEY (id_car) REFERENCES car_rental.car (id_car),
  FOREIGN KEY (id_rent) REFERENCES car_rental.rent (id_rent)
);


-- -----------------------------------------------------
-- Table car_rental.form
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.form ;

CREATE TABLE IF NOT EXISTS car_rental.form (
  id_form TINYINT(1) NOT NULL,
  name VARCHAR(45) NOT NULL,
  description VARCHAR(256) NULL,
  PRIMARY KEY (id_form)
);


-- -----------------------------------------------------
-- Table car_rental.billing_forms
-- -----------------------------------------------------
DROP TABLE IF EXISTS car_rental.billing_forms ;

CREATE TABLE IF NOT EXISTS car_rental.billing_forms (
  id_billing INT NOT NULL,
  id_form TINYINT(1) NOT NULL,
  value DECIMAL(6,2) NOT NULL,
  FOREIGN KEY (id_billing) REFERENCES car_rental.billing (id_billing),
  FOREIGN KEY (id_form) REFERENCES car_rental.form (id_form)
);
