USE dc_db;

# Inserção de novo funcionário

SET autocommit=FALSE;
START TRANSACTION;
INSERT INTO dc_db.person VALUES(NULL, "José da Silva", "1998-07-03", "Rua Oyapock", 25, "Cristo Rei", 12562844501, "M");
SET @employee_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.employee VALUES(@person_id, 1, "Médico", "09:00:00", "18:00:00");
COMMIT;

# Inserção de nova bolsa de sangue de novo paciente

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

# Inseção de um recebedor novo

SET autocommit=FALSE;
START TRANSACTION;
INSERT INTO dc_db.person VALUES(NULL, "Leonardo Gomez", "1996-05-24", "Rua dos Palotinos", 58, "Jardim Botânico", 59842731026, "M");
SET @receiver_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.receiver VALUES(@receiver_id, 7, NOW(), "O+");
SET @receive_date := (SELECT r.date_receive FROM dc_db.receiver r WHERE r.id_receiver = @receiver_id); 
UPDATE dc_db.blood_bags b SET b.departure_date = @receive_date WHERE b.id_bags = 7;
COMMIT;

# Inserção de um pagamento novo

SET autocommit=FALSE;
START TRANSACTION;
INSERT INTO dc_db.payment VALUES(NULL, 7, 1500.00, CURDATE());
SET @payment_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.desconts VALUES(NULL, 200.00, "Multa");
SET @descount_id := (SELECT LAST_INSERT_ID());
INSERT INTO dc_db.payment_desconts VALUES(@payment_id, @descount_id);
COMMIT;