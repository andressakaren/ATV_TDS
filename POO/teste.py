# Criar uma companhia
companhia = CompanhiaAerea("Sky Airlines")

print(companhia.nome)
# companhia.listar_voos()

# Cadastra voo1
voo1 = Voo(101, 'São Paulo', 'Teresina')

companhia.adicionar_voo(voo1)
# companhia.listar_voos()

# Cadastra voo2
voo2 = Voo(202, 'Xique Xique', 'Belo Horizonte')
companhia.adicionar_voo(voo2)
# companhia.listar_voos()


### CADASTRAR PASSAGEIROS
passageiro1 = Passageiro('Kallya', '57427651344')
passageiro2 = Passageiro('Carlos', '54622255468')
passageiro3 = Passageiro('luiz', '78955532684')

## CRIANDO CLASSES
economica_sem_bag = ClasseEconomica(500, False)
economica_com_bag = ClasseEconomica(500, True)
executiva_nivel1 = ClasseExecutiva(1500, 'Refeição completa')
executiva_nivel2 = ClasseExecutiva(2000, 'All inclusive')

## ADD as classes ao respectivo voo
voo1.adicionar_passagem(passageiro1, economica_com_bag)
voo1.adicionar_passagem(passageiro2, economica_sem_bag)
voo2.adicionar_passagem(passageiro3, executiva_nivel2)

companhia.listar_voos()