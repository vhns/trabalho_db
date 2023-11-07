
--  Procedimento para Inserção de Paciente:

DELIMITER //
CREATE PROCEDURE InsertPacient(IN p_name VARCHAR(100), IN p_blood_type VARCHAR(3))
BEGIN
    INSERT INTO dc_db.pacient (blood_type)
    VALUES (p_name, p_blood_type);
END //
DELIMITER ;

-- Procedimento com uso de Cursor:
DELIMITER //
CREATE PROCEDURE UpdateAllEmployees()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE employee_id INT;
    DECLARE cur CURSOR FOR SELECT id_employee FROM dc_db.employee;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO employee_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        -- Atualização desejada
        UPDATE dc_db.employee SET working_period_s = '09:00:00' WHERE id_employee = employee_id;
    END LOOP;
    CLOSE cur;
END //
DELIMITER ;

-- Procedimento para Exclusão de Registros:


    DELIMITER //
    CREATE PROCEDURE DeletePersonAndRelatedData(IN p_id INT)
    BEGIN
        DELETE FROM dc_db.person WHERE id_person = p_id;
        DELETE FROM dc_db.employee WHERE id_employee = p_id;
        DELETE FROM dc_db.receiver WHERE id_receiver = p_id;
        -- ... outras tabelas relacionadas
    END //
    DELIMITER ;

--  Função para Calcular Idade:


DELIMITER //
CREATE FUNCTION CalculateAge(p_birth_year DATE) RETURNS INT
BEGIN
    RETURN YEAR(CURDATE()) - YEAR(p_birth_year);
END //
DELIMITER ;

-- Função para Obter o Centro de Doação:


DELIMITER //
CREATE FUNCTION GetDonationCenterName(p_id INT) RETURNS VARCHAR(45)
BEGIN
    DECLARE center_name VARCHAR(45);
    SELECT center_name INTO center_name FROM dc_db.donation_center WHERE id_center = p_id;
    RETURN center_name;
END //
DELIMITER ;

-- Função para Contar Bolsas de Sangue:

DELIMITER //
CREATE FUNCTION CountBloodBags() RETURNS INT
BEGIN
    DECLARE total_bags INT;
    SELECT COUNT(id_bags) INTO total_bags FROM dc_db.blood_bags;
    RETURN total_bags;
END //
DELIMITER ;
