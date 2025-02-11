SET search_path TO lista6;
-- INSERÇÃO DE 3 DEPARTAMENTOS: --
-- 1. Marketing com número de departamento 404
-- 2. Juridico com número de departamento 505
-- 3. Inserção de funcionarios

INSERT INTO departamentos VALUES (404, 'Marketing');

INSERT INTO departamentos (nome, numero_departamento) VALUES ('Juridico', 505);

INSERT INTO funcionarios VALUES 
	('22222222226', 'Andressa Karen', 'F', 4000.00, 303),
	('44444444441', 'Maria', 'F', 6000.00, 404),
	('55555555551', 'Joao Pedro', 'M', 785.00, 505);
	
-- Liste todos os departamentos mostrando todos os atributos
SELECT 	* 
FROM 	departamentos;

-- Liste todos os funcionários mostrando todos os atributos
SELECT 	* 
FROM 	funcionarios;

-- Liste todos os funcionários mostrando nome e salários.
SELECT 		nome, salario
FROM 		funcionarios
ORDER BY 	nome;

-- Selecionar todos os funcionários que ganham igual ou acima de 3000.00.
SELECT 	nome, salario
FROM	funcionarios
WHERE	salario >= 3000.00;

-- Selecionar todos os funcionários que são homens e ganham igual ou acima de 3000
SELECT	*
FROM	funcionarios
WHERE	sexo = 'M' AND salario >= 3000.00;

-- Selecionar todos os funcionários do departamento de vendas.
SELECT	*
FROM	funcionarios
WHERE	numero_departamento = 101;

SELECT	f.*
FROM	funcionarios f, departamentos d
WHERE	f.numero_departamento = d.numero_departamento AND d.nome = 'Vendas';

-- Selecionar todos os funcionárois do departamento de estoque e são do sexo masculino

SELECT	f.*
FROM	funcionarios f
WHERE	f.numero_departamento = 202 AND f.sexo = 'M';

-- Selecionar todos os funcionários do departamento de estoque e vendas.

SELECT	f.*
FROM	funcionarios f
WHERE	f.numero_departamento IN (202, 101);

--  Remover todos os funcionários que ganham igual a 4100.00 ou mais.

DELETE FROM funcionarios
WHERE salario >= 4000.00 AND numero_departamento = 303
