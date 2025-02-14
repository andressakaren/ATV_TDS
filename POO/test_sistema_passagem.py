
import pytest
from sistema_passagem import CompanhiaAerea, Voo, PassagemAerea, Passageiro, ClasseVoo, ClasseEconomica, ClasseExecutiva

# Testes para a CompanhiaAerea

def test_criar_companhia_valida():
    companhia = CompanhiaAerea("Sky Airlines")
    assert companhia.nome == "Sky Airlines"

# def test_criar_companhia_nome_vazio():
#     companhia = CompanhiaAerea("")
#     assert companhia.nome != ""  # A companhia não deve ser criada com nome vazio

def test_adicionar_voo_unico():
    companhia = CompanhiaAerea("Sky Airlines")
    voo = Voo("SA123", "São Paulo", "Rio de Janeiro")
    companhia.adicionar_voo(voo)
    assert len(companhia.voos) == 1
    assert companhia.voos[0].numero == "SA123"

def test_adicionar_voo_duplicado():
    companhia = CompanhiaAerea("Sky Airlines")
    voo = Voo("SA123", "São Paulo", "Rio de Janeiro")
    companhia.adicionar_voo(voo)
    voo_duplicado = Voo("SA123", "São Paulo", "Rio de Janeiro")
    companhia.adicionar_voo(voo_duplicado)
    assert len(companhia.voos) == 1  # O voo duplicado não deve ser adicionado

def test_listar_voos_vazia():
    companhia = CompanhiaAerea("Sky Airlines")
    companhia.listar_voos()
    # Verifique a saída, deve ser "Nenhum voo cadastrado!"

def test_listar_voos_com_voos():
    companhia = CompanhiaAerea("Sky Airlines")
    voo = Voo("SA123", "São Paulo", "Rio de Janeiro")
    companhia.adicionar_voo(voo)
    companhia.listar_voos()
    # Verifique a exibição dos voos na saída


# Testes para a classe Voo

def test_criar_voo_valido():
    voo = Voo("SA123", "São Paulo", "Rio de Janeiro")
    assert voo.numero == "SA123"
    assert voo.origem == "São Paulo"
    assert voo.destino == "Rio de Janeiro"

def test_adicionar_passagem_com_sucesso():
    voo = Voo("SA123", "São Paulo", "Rio de Janeiro")
    passageiro = Passageiro("João", "12345678901")
    classe = ClasseEconomica(500, False)
    voo.adicionar_passagem(passageiro, classe)
    assert len(voo.passagens) == 1

def test_adicionar_passagem_voo_lotado():
    voo = Voo("SA123", "São Paulo", "Rio de Janeiro")
    passageiro1 = Passageiro("João", "12345678901")
    passageiro2 = Passageiro("Maria", "12345678902")
    passageiro3 = Passageiro("Carlos", "12345678903")
    passageiro4 = Passageiro("Ana", "12345678904")
    passageiro5 = Passageiro("Pedro", "12345678905")
    
    classe = ClasseEconomica(500, False)
    voo.adicionar_passagem(passageiro1, classe)
    voo.adicionar_passagem(passageiro2, classe)
    voo.adicionar_passagem(passageiro3, classe)
    voo.adicionar_passagem(passageiro4, classe)
    voo.adicionar_passagem(passageiro5, classe)  # Deve falhar

    assert len(voo.passagens) == 4  # O voo não pode ter mais de 4 passagens

def test_calcular_total_arrecadado():
    voo = Voo("SA123", "São Paulo", "Rio de Janeiro")
    passageiro = Passageiro("João", "12345678901")
    classe = ClasseEconomica(500, False)
    voo.adicionar_passagem(passageiro, classe)
    assert voo.calcular_total_arrecadado() == 500

# Testes para a classe PassagemAerea

def test_criar_passagem():
    passageiro = Passageiro("João", "12345678901")
    classe = ClasseEconomica(500, False)
    passagem = PassagemAerea(passageiro, classe)
    assert passagem.passageiro.nome == "João"
    assert passagem.classe.calcular_preco() == 500

def test_exibir_detalhes_passagem():
    passageiro = Passageiro("João", "12345678901")
    classe = ClasseEconomica(500, False)
    passagem = PassagemAerea(passageiro, classe)
    passagem.exibir_detalhes()
    # Verifique a saída para garantir que os detalhes estão sendo exibidos corretamente


# Testes para a classe Passageiro

def test_criar_passageiro_valido():
    passageiro = Passageiro("João", "12345678901")
    assert passageiro.nome == "João"
    assert passageiro.documento == "12345678901"

def test_criar_passageiro_cpf_invalido():
    with pytest.raises(Exception):  # Exceção deve ser levantada no método de validação de CPF
        passageiro = Passageiro("João", "1234567890")  # CPF inválido

# Testes para as classes ClasseVoo, ClasseEconomica e ClasseExecutiva

def test_calcular_preco_classe_economica():
    classe = ClasseEconomica(500, False)
    assert classe.calcular_preco() == 500

def test_calcular_preco_classe_economica_com_bagagem():
    classe = ClasseEconomica(500, True)
    assert classe.calcular_preco() == 700

def test_calcular_preco_classe_executiva():
    classe = ClasseExecutiva(1500, "Refeição completa")
    assert classe.calcular_preco() == 2500