SET search_path TO lista9;

-- Questao 01 --
-- Selecionar a quantidade de emprestimos feitos pelo aluno 
-- com id = 2

SELECT	COUNT(e.id)
FROM	emprestimo e
WHERE	e.id_aluno = 2;
-- 4


-- Questao 02 -- 
-- Selecionar os titulos dos livros que já foram emprestados 
-- ao aluno com id = 2

SELECT 	l.titulo
FROM 	livro l, emprestimo e
WHERE 	l.id = e.id_livro 
	AND	e.id_aluno = 2;
-- Total rows: 4


-- Questao 03 --
-- Listar o nome do aluno e o titulo do 
-- livro para cada emprestimo realizado

SELECT 	a.nome, l.titulo
FROM 	aluno a, livro l, emprestimo e
WHERE	l.id = e.id_livro AND
		e.id_aluno = a.id;
-- Total rows: 20


-- Questao 04 --
-- Listar o nome do autor e o titulo de 
-- todos os livros que ele escreveu

SELECT	au.nome, l.titulo
FROM	autor au, livro l, livro_autor la 
WHERE 	au.id = la.id_autor AND
		la.id_livro = l.id;
-- Total rows: 20


-- Questao 05 --
-- Listar a quantidade de emprestimos de 
-- livros escritos pelo Machado de Assis

SELECT	COUNT(e.id)
FROM	emprestimo e, autor au, livro_autor la, livro l
WHERE	au.nome = 'Machado de Assis' AND
		au.id = la.id_autor AND
		la.id_livro = l.id AND
		l.id = e.id_aluno;
-- 12