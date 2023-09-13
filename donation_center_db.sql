drop schema if exists dc_db;
create schema if not exists dc_db;

-- ------ Pessoas ------

create table if not exists dc_db.person(
	id_person int unsigned not null auto_increment,
	person_name varchar(100) not null,
    birth_year date not null,
    street varchar(100) not null,
    house_number smallint not null,
	neighborhood varchar(45) not null,
    cpf char(11) not null unique,
    sex char(1) not null,
    primary key(id_person)
);

-- ----- Pacientes ------

create table if not exists dc_db.pacient(
	id_pacient int unsigned not null,
    blood_type varchar(3) not null,
    primary key(id_pacient),
    foreign key(id_pacient) references dc_db.person(id_person)
);

-- ------ Centro ------

create table if not exists dc_db.donation_center(
	id_center int unsigned not null auto_increment,
    center_name varchar(45) not null,
    street varchar(100) not null,
    center_number smallint not null,
    neighborhood varchar(45) not null,
    working_period_s time not null,
    working_period_e time not null,
    primary key(id_center)
);

-- ------ Pacient_Center ------

create table if not exists dc_db.pacient_center(
	id_pacient int unsigned not null,
    id_center int unsigned not null,
    primary key(id_pacient),
    foreign key(id_pacient) references dc_db.pacient(id_pacient),
    foreign key(id_center) references dc_db.donation_center(id_center)
);

-- ------ Estoque ------

create table if not exists dc_db.storage(
	id_storage int unsigned not null auto_increment,
    id_center int unsigned not null,
    street varchar(100) not null,
    s_number smallint not null,
    neighborhood varchar(45) not null,
    primary key(id_storage),
    foreign key(id_center) references dc_db.donation_center(id_center)
);

-- ------ Funcionario ------

create table if not exists dc_db.employee(
	id_employee int unsigned not null,
    id_donation_center int unsigned not null,
    e_function varchar(45) not null,
    working_period_s time not null,
    working_period_e time not null,
    primary key(id_employee),
    foreign key(id_employee) references dc_db.person(id_person),
    foreign key(id_donation_center) references dc_db.donation_center(id_center)
);

-- ------ Bolsas de Sangue ------

create table if not exists dc_db.blood_bags(
	id_bags int unsigned not null auto_increment,
    id_employee int unsigned not null,
    id_pacient int unsigned not null,
    blood_type varchar(3) not null,
    entry_date datetime not null,
    departura_date datetime not null,
    primary key(id_bags),
    foreign key(id_employee) references dc_db.employee(id_employee),
    foreign key(id_pacient) references dc_db.pacient(id_pacient)
);

-- ------ blood_storage ------

create table if not exists dc_db.blood_storage(
	id_bags int unsigned not null,
    id_storage int unsigned not null,
    primary key(id_bags),
    foreign key(id_bags) references dc_db.blood_bags(id_bags),
    foreign key(id_storage) references dc_db.storage(id_storage)
);

-- ------ Recebedor ------

create table if not exists dc_db.receiver(
	id_receiver int unsigned not null,
    id_bags int unsigned not null,
    date_receive datetime not null,
    blood_type varchar(3) not null,
    primary key(id_receiver),
    foreign key(id_receiver) references dc_db.person(id_person),
    foreign key(id_bags) references dc_db.blood_bags(id_bags)
);

-- ------ Receiver_Center ------

create table if not exists dc_db.receiver_center(
	id_receiver int unsigned not null,
    id_center int unsigned not null,
    primary key(id_receiver),
    foreign key(id_receiver) references dc_db.receiver(id_receiver),
    foreign key(id_center) references dc_db.donation_center(id_center) 
);

-- ------ Pagamentos ------

create table if not exists dc_db.payment(
	id_payment int unsigned not null auto_increment,
    id_employee int unsigned not null,
    payment_value decimal(6,2) unsigned not null,
    payment_date date not null,
    primary key(id_payment),
    foreign key(id_employee) references dc_db.employee(id_employee)
);

-- ------ Descontos ------

create table if not exists dc_db.desconts(
	id_descont int unsigned not null auto_increment,
    descont_value decimal(6,2) not null,
    descont_description varchar(45) not null,
    primary key(id_descont)
);

-- ------ Descontos dos pagamentos ------

create table if not exists dc_db.payment_desconts(
	id_descont int unsigned not null,
    id_payment int unsigned not null,
    primary key(id_payment),
    foreign key(id_payment) references dc_db.payment(id_payment),
    foreign key(id_descont) references dc_db.desconts(id_descont)
);


