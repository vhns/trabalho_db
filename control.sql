CREATE USER 'vitor'@'127.0.0.1' IDENTIFIED BY 'vitor123';
CREATE USER 'joao'@'127.0.0.1' IDENTIFIED BY 'joao123';
CREATE USER 'marco'@'127.0.0.1' IDENTIFIED BY 'marco123';
CREATE USER 'henrique'@'127.0.0.1' IDENTIFIED BY 'henrique123';
CREATE USER 'antonio'@'127.0.0.1' IDENTIFIED BY 'antonio123';
CREATE USER 'cleber'@'127.0.0.1' IDENTIFIED BY 'cleber123';

CREATE ROLE 'Admin', 'Gestor', 'Coletor', 'rh';

GRANT all on *.* to 'Admin'; -- Role criado para o administrador de todos os bancos 

GRANT ALL ON dc_db to 'Gestor'; -- Role criado para o gestor dos centros de doaçoes

GRANT INSERT, UPDATE ON dc_db.blood_bags to 'Coletor'; -- Role criado para permitir que funcionarios coletores possam inserir as bolsas de sangue no
													   -- banco de dados

GRANT INSERT ON dc_db.payment 	TO 'rh'; -- Role criado para que os funcionarios do rh possam fazer os pagamentos de todos os funcionarios
GRANT INSERT ON dc_db.payment_desconts 	TO 'rh';
GRANT INSERT ON dc_db.desconts TO 'rh';

grant 'Admin' to 'antonio'@'127.0.0.1';
show grants for 'antonio'@'127.0.0.1';

grant 'Gestor' to 'cleber'@'127.0.0.1';
show grants for 'cleber'@'127.0.0.1';

grant 'Coletor' to 'joao'@'127.0.0.1', 'vitor'@'127.0.0.1';
show grants for 'joao'@'127.0.0.1';
show grants for 'vitor'@'127.0.0.1';

grant 'rh' to 'marco'@'127.0.0.1', 'henrique'@'127.0.0.1';
show grants for 'marco'@'127.0.0.1';
show grants for 'henrique'@'127.0.0.1';

