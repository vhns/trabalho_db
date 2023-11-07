-- Inserir 6 registros na tabela person:


INSERT INTO dc_db.person (person_name, birth_year, street, house_number, neighborhood, cpf, sex)
VALUES 
('João', '1990-05-15', 'Rua A', 10, 'Centro', '12345678901', 'M'),
('Maria', '1985-08-22', 'Rua B', 20, 'Bairro X', '23456789012', 'F'),
('Carlos', '1978-03-10', 'Rua C', 15, 'Bairro Y', '34567890123', 'M'),
('Ana', '1995-12-03', 'Rua D', 25, 'Centro', '45678901234', 'F'),
('Pedro', '1980-07-18', 'Rua E', 30, 'Bairro Z', '56789012345', 'M'),
('Sofia', '1992-11-29', 'Rua F', 5, 'Bairro W', '67890123456', 'F');

--  Inserir 6 registros na tabela pacient:


INSERT INTO dc_db.pacient (id_pacient, blood_type)
VALUES 
(1, 'A+'),
(2, 'B-'),
(3, 'O+'),
(4, 'AB+'),
(5, 'A-'),
(6, 'B+');

--  Inserir 6 registros na tabela donation_center:


INSERT INTO dc_db.donation_center (center_name, street, center_number, neighborhood, working_period_s, working_period_e)
VALUES 
('Centro A', 'Rua Principal', 50, 'Centro', '08:00:00', '17:00:00'),
('Centro B', 'Avenida X', 30, 'Bairro Y', '09:00:00', '18:00:00'),
('Centro C', 'Rua Z', 20, 'Bairro W', '08:30:00', '16:30:00'),
('Centro D', 'Avenida Principal', 100, 'Centro', '07:00:00', '16:00:00'),
('Centro E', 'Rua Y', 40, 'Bairro X', '09:30:00', '18:30:00'),
('Centro F', 'Avenida A', 15, 'Bairro Z', '08:15:00', '17:15:00');

-- Inserir 6 registros na tabela storage:


INSERT INTO dc_db.storage (id_center, street, s_number, neighborhood)
VALUES 
(1, 'Rua Principal', 1, 'Centro'),
(2, 'Avenida X', 2, 'Bairro Y'),
(3, 'Rua Z', 3, 'Bairro W'),
(4, 'Avenida Principal', 4, 'Centro'),
(5, 'Rua Y', 5, 'Bairro X'),
(6, 'Avenida A', 6, 'Bairro Z');

-- Inserir 6 registros na tabela employee:


INSERT INTO dc_db.employee (id_employee, id_donation_center, e_function, working_period_s, working_period_e)
VALUES 
(1, 1, 'Enfermeiro', '08:00:00', '17:00:00'),
(2, 2, 'Médico', '09:00:00', '18:00:00'),
(3, 3, 'Atendente', '08:30:00', '16:30:00'),
(4, 4, 'Enfermeiro', '07:00:00', '16:00:00'),
(5, 5, 'Atendente', '09:30:00', '18:30:00'),
(6, 6, 'Médico', '08:15:00', '17:15:00');

-- Inserir 6 registros na tabela blood_bags:

INSERT INTO dc_db.blood_bags (id_employee, id_pacient, blood_type, entry_date, departure_date)
VALUES 
(1, 1, 'A+', '2023-10-01 08:00:00', '2023-10-05 17:00:00'),
(2, 2, 'B-', '2023-10-02 09:00:00', '2023-10-06 18:00:00'),
(3, 3, 'O+', '2023-10-03 08:30:00', '2023-10-07 16:30:00'),
(4, 4, 'AB+', '2023-10-04 07:00:00', '2023-10-08 16:00:00'),
(5, 5, 'A-', '2023-10-05 09:30:00', '2023-10-09 18:30:00'),
(6, 6, 'B+', '2023-10-06 08:15:00', '2023-10-10 17:15:00');



-- Atualizar um registro na tabela person:


UPDATE dc_db.person
SET person_name = 'Novo Nome'
WHERE id_person = 1;



-- Atualizar um registro na tabela donation_center:


UPDATE dc_db.donation_center
SET center_name = 'Novo Centro'
WHERE id_center = 1;

-- Atualizar um registro na tabela employee:


UPDATE dc_db.employee
SET e_function = 'Novo Cargo'
WHERE id_employee = 1;

-- Atualizar um registro na tabela blood_bags:


UPDATE dc_db.blood_bags
SET blood_type = 'A-'
WHERE id_bags = 1;

-- Atualizar um registro na tabela pacient:


UPDATE dc_db.pacient
SET blood_type = 'AB-'
WHERE id_pacient = 1;
