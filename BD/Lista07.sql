SET search_path TO lista7;

-- Listar todos os alunos com seus respectivos ids, nomes e datas de nascimento.

SELECT	*
FROM	aluno;

-- Exibir o nome e a carga horária das disciplinas com carga horária superior a 50 horas.

SELECT 	d.nome, d.carga_horaria
FROM 	disciplina d
WHERE 	d.carga_horaria > 50;

-- Mostrar as disciplinas nas quais o aluno com ID 10 está matriculado.

SELECT	d.nome
FROM	disciplina d, matricula m
WHERE	d.disciplina_id = m.disciplina_id AND aluno_ID = 10;

-- Listar o nome, as médias e faltas de todos os alunos em uma disciplina específica 
-- (ex:Matemática) ordenados por nome.

SELECT	a.nome, m.faltas, m.media
FROM	aluno a, matricula m, disciplina d
WHERE	d.nome = 'Matemática' 
	AND d.disciplina_id = m.disciplina_id
	AND m.aluno_id = a.aluno_id
ORDER BY a.nome;

-- Listar, para todas as disciplinas, o nome da disciplina e o nome do aluno com média maior
-- ou igual a 7 naquela disciplina, com agrupamento por aluno.

SELECT	d.nome, a.nome
FROM	aluno a, matricula m, disciplina d
WHERE	m.media >= 7 
	AND d.disciplina_id = m.disciplina_id
	AND m.aluno_id = a.aluno_id;