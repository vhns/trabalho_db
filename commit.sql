USE dc_db;

-- Inserção de novo funcionário

SET autocommit=FALSE;
START TRANSACTION;
INSERT INTO dc_db.person VALUES(NULL, "José da Silva", "1998-07-03", "Rua Oyapock", 25, "Cristo Rei", 12562844501, "M");
SET @employee_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.employee VALUES(@person_id, 1, "Médico", "09:00:00", "18:00:00");
COMMIT;

-- Inserção de nova bolsa de sangue de novo paciente

SET autocommit=FALSE;
START TRANSACTION;
INSERT INTO dc_db.person VALUES(NULL, "Mariana Mendes", "1985-11-08", "Avenida Presidente Kennedy", 63, "Água Verde", 20562634895, "F");
SET @pacient_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.pacient VALUES(@pacient_id, "O+");
SET @pacient_blood_type := (SELECT p.blood_type FROM dc_db.pacient p WHERE p.id_pacient = @pacient_id);
INSERT INTO dc_db.blood_bags VALUES(NULL, 2, @pacient_id, @pacient_blood_type, NOW(), NULL);
SET @blood_bag_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.blood_storage VALUES(@blood_bag_id, 2);
COMMIT;

-- Inseção de um recebedor novo

SET autocommit=FALSE;
START TRANSACTION;
INSERT INTO dc_db.person VALUES(NULL, "Leonardo Gomez", "1996-05-24", "Rua dos Palotinos", 58, "Jardim Botânico", 59842731026, "M");
SET @receiver_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.receiver VALUES(@receiver_id, 7, NOW(), "O+");
SET @receive_date := (SELECT r.date_receive FROM dc_db.receiver r WHERE r.id_receiver = @receiver_id); 
UPDATE dc_db.blood_bags b SET b.departure_date = @receive_date WHERE b.id_bags = 7;
COMMIT;

-- Inserção de um pagamento novo

SET autocommit=FALSE;
START TRANSACTION;
INSERT INTO dc_db.payment VALUES(NULL, 7, 1500.00, CURDATE());
SET @payment_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.desconts VALUES(NULL, 200.00, "Multa");
SET @descount_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.payment_desconts VALUES(@payment_id, @descount_id);
COMMIT;

-- Pegar informação dos sacos de sangue

SELECT bb.id_bags, bb.blood_type, bb.entry_date, bb.departura_date, 
       e.person_name AS employee_name, p.person_name AS patient_name
FROM dc_db.blood_bags bb
JOIN dc_db.employee e ON bb.id_employee = e.id_employee
JOIN dc_db.pacient p ON bb.id_pacient = p.id_pacient;

-- Juntar a informação do funcionário com o centro de doação

SELECT emp.person_name AS employee_name, emp.e_function, dc.center_name
FROM dc_db.employee emp
JOIN dc_db.donation_center dc ON emp.id_donation_center = dc.id_center;

-- Juntar informação do recebedor/paciente com o centro de doação

SELECT r.person_name AS receiver_name, rc.date_receive, bb.blood_type, dc.center_name
FROM dc_db.receiver r
JOIN dc_db.receiver_center rc ON r.id_receiver = rc.id_receiver
JOIN dc_db.blood_bags bb ON rc.id_bags = bb.id_bags
JOIN dc_db.donation_center dc ON rc.id_center = dc.id_center;

-- Junta informação de pagamento com os descontos
SELECT p.id_payment, emp.person_name AS employee_name, p.payment_value, p.payment_date,
       d.descont_description, d.descont_value
FROM dc_db.payment p
JOIN dc_db.employee emp ON p.id_employee = emp.id_employee
LEFT JOIN dc_db.payment_desconts pd ON p.id_payment = pd.id_payment
LEFT JOIN dc_db.desconts d ON pd.id_descont = d.id_descont;

START TRANSACTION;
SAVEPOINT salvamento1;
INSERT INTO dc_db.person (person_name, birth_year, street, house_number, neighborhood, cpf, sex)
VALUES 
('Thiago', '1990-05-15', 'Rua A', 100, 'Centro', '12345678901', 'M');
ROLLBACK TO SAVEPOINT salvamento1;
COMMIT;

START TRANSACTION;
SAVEPOINT salvamento2;
INSERT INTO dc_db.person (person_name, birth_year, street, house_number, neighborhood, cpf, sex)
VALUES 
('Ricardo', '1990-05-15', 'Rua A', 1002, 'Centro', '12345678901', 'M');
ROLLBACK TO SAVEPOINT salvamento2;
COMMIT;

START TRANSACTION;
INSERT INTO dc_db.pacient (id_pacient, blood_type)
VALUES 
(7, 'B-');
ROLLBACK;
COMMIT;

START TRANSACTION;
INSERT INTO dc_db.pacient (id_pacient, blood_type)
VALUES 
(8, 'O-');
ROLLBACK;
COMMIT;

START TRANSACTION;
INSERT INTO dc_db.storage (id_center, street, s_number, neighborhood)
VALUES 
(7, 'Rua Principal', 7, 'Centro');
ROLLBACK;
COMMIT;

START TRANSACTION;
INSERT INTO dc_db.storage (id_center, street, s_number, neighborhood)
VALUES 
(8, 'Rua Principal', 8, 'Centro');
ROLLBACK;
COMMIT;
