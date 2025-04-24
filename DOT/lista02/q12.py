# 12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E.
# Para isso são dados: o cartão gabarito; o número de alunos da turma;
# o cartão de respostas para cada aluno, contendo o seu número e suas respostas.

def corrigir_provas():
    gabarito = []
    for i in range(30):
        letra = input(f"Digite a resposta correta da questão {i+1} (A/B/C/D/E): ").upper()
        gabarito.append(letra)

    num_alunos = int(input("Digite o número de alunos: "))
    for aluno in range(num_alunos):
        print(f"\nAluno {aluno+1}:")
        acertos = 0
        for i in range(30):
            resposta = input(f"Resposta da questão {i+1}: ").upper()
            if resposta == gabarito[i]:
                acertos += 1
        print(f"Aluno {aluno+1} acertou {acertos} questões.")

corrigir_provas()
