SET search_path TO lista8;

---- QUESTAO 01 ----
-- Encontrar o nome e valor de todos os produtos com preço superior a 10.0.

SELECT	p.nome, p.preco
FROM	produtos p
WHERE	p.preco > 10.0;
-- Total rows: 13

---- QUESTAO 02 ----
-- Listar a data de todos os pedidos feitos por um cliente específico, 
-- identificado pelo cliente com id = 2.

SELECT	pe.data_pedido, c.nome
FROM	pedidos pe, clientes c
WHERE	c.id_cliente = 2
	AND c.id_cliente = pe.id_cliente;
-- Total rows: 3

---- QUESTAO 03 ----
-- Listar a quantidade de pedidos realizados pelo cliente com id = 3.

SELECT	COUNT(pe.*)
FROM	pedidos pe
WHERE	pe.id_cliente = 3;
-- Total rows: 1
-- Count: 3

---- QUESTAO 04 ----
-- Listar o nome, quantidade e preço unitário dos produtos que foram comprados em um
-- pedido específico (id_pedido = 1)

SELECT	p.nome, pp.quantidade, pp.preco_unitario
FROM	produtos p, pedidos_produtos pp
WHERE    pp.id_pedido = 1
	AND pp.id_produto = p.id_produto;
-- Total rows: 5

---- QUESTAO 05 ----
-- Listar a quantidade de pedidos realizados pelo cliente com nome = ‘Beltrano’.

SELECT	COUNT(pe.id_pedido)
FROM	pedidos pe, clientes c
WHERE	c.nome = 'Beltrano' 
	AND pe.id_cliente = c.id_cliente;
-- Total rows: 1
-- Count: 3

---- QUESTAO 06 ----
-- Calcular o valor total do pedido com id = 2.

SELECT	SUM(pp.preco_unitario * pp.quantidade)
FROM	pedidos pe, pedidos_produtos pp
WHERE	pe.id_pedido = 2 
	AND pe.id_pedido = pp.id_pedido;
-- 448.50

---- QUESTAO 07 ----
-- Calcular o valor total de todos os pedidos do cliente com id = 1.

SELECT	SUM(pp.preco_unitario * pp.quantidade)
FROM	pedidos pe, clientes c, pedidos_produtos pp
WHERE	c.id_cliente = 1 
	AND pe.id_cliente = c.id_cliente
	AND pe.id_pedido = pp.id_pedido;
-- 938.50
