-- 1 - Quantidade de pacientes por mês/dia/ano:
SELECT COUNT(id_pacient) AS num_pacients, 
       MONTH(entry_date) AS month, 
       DAY(entry_date) AS day, 
       YEAR(entry_date) AS year
FROM dc_db.blood_bags
GROUP BY YEAR(entry_date), MONTH(entry_date), DAY(entry_date);

-- 2 - Número total de bolsas de sangue:
SELECT COUNT(id_bags) AS total_blood_bags
FROM dc_db.blood_bags;

-- 3 - Número de bolsas de sangue por tipo sanguíneo:
SELECT blood_type, COUNT(id_bags) AS total_blood_bags
FROM dc_db.blood_bags
GROUP BY blood_type;

-- 4 - Quantidade de bolsas que expiram no mês seguinte:
SELECT COUNT(id_bags) AS expiring_next_month
FROM dc_db.blood_bags
WHERE MONTH(departure_date) = MONTH(CURDATE()) + 1;

-- 5 - Quantidade de bolsas que expiram no mês seguinte por tipo sanguíneo:
SELECT blood_type, COUNT(id_bags) AS expiring_next_month
FROM dc_db.blood_bags
WHERE MONTH(departure_date) = MONTH(CURDATE()) + 1
GROUP BY blood_type;

-- 6 - Valor total de salário mensal:
SELECT SUM(payment_value) AS total_monthly_salary
FROM dc_db.payment
WHERE MONTH(payment_date) = MONTH(CURDATE());

-- 7 - Valor total de salário anual:
SELECT SUM(payment_value) AS total_annual_salary
FROM dc_db.payment
WHERE YEAR(payment_date) = YEAR(CURDATE());

-- 8 - Número total de funcionários:
SELECT COUNT(id_employee) AS total_employees
FROM dc_db.employee;

-- 10 - Espaço livre no estoque:
SELECT COUNT(id_storage) AS free_space
FROM dc_db.storage
WHERE id_storage NOT IN (SELECT id_storage FROM dc_db.blood_storage);

-- 11 - Espaço ocupado no estoque:
SELECT COUNT(id_storage) AS occupied_space
FROM dc_db.blood_storage;

-- 12 - Quantidade de pacientes atendidos por centro de doação:
SELECT pc.id_center, COUNT(bb.id_pacient) AS num_pacients_handled
FROM dc_db.pacient_center pc
JOIN dc_db.blood_bags bb ON pc.id_pacient = bb.id_pacient
GROUP BY pc.id_center;

-- 13 - Quantidade de bolsas que saíram por centro de doação:
SELECT id_center, COUNT(id_bags) AS num_bags_departed
FROM dc_db.blood_storage
GROUP BY id_center;

-- 14 - Quantidade em litros de sangue:
SELECT COUNT(id_bags) AS total_volume_liters
FROM dc_db.blood_bags;

-- 15 - Quantidade em litros de sangue por tipo sanguíneo:
SELECT blood_type, COUNT(id_bags) AS total_volume_liters
FROM dc_db.blood_bags
GROUP BY blood_type;

-- 16 - Média de bolsas de sangue por paciente:
SELECT AVG(num_bags) AS avg_bags_per_patient
FROM (SELECT id_pacient, COUNT(id_bags) AS num_bags
      FROM dc_db.blood_bags
      GROUP BY id_pacient) AS bags_per_patient;

-- 17 - Quantidade de doadores por tipo sanguíneo:
SELECT blood_type, COUNT(id_person) AS num_donors
FROM dc_db.person
GROUP BY blood_type;

-- 18 - Número de bolsas por ano e tipo sanguíneo:
SELECT YEAR(entry_date) AS year, blood_type, COUNT(id_bags) AS total_bags
FROM dc_db.blood_bags
GROUP BY YEAR(entry_date), blood_type;

-- 19 - Média de salário por tipo de funcionário:
SELECT e_function, AVG(payment_value) AS avg_salary
FROM dc_db.employee
JOIN dc_db.payment ON employee.id_employee = payment.id_employee
GROUP BY e_function;

-- 20 - Número de recebedores por centro de doação:
SELECT rc.id_center, COUNT(r.id_receiver) AS num_receivers
FROM dc_db.receiver_center rc
JOIN dc_db.receiver r ON rc.id_receiver = r.id_receiver
GROUP BY rc.id_center;

