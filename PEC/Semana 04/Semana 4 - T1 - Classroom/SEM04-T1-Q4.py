print('Você gostaria de saber quantos segundos se passaram desde a meia-noite?')
hora = int(input('Digite o valor, em horas: '))
minuto = int(input('Digite o valor, em minutos: '))
segundo = int(input('Digite o valor, em segundos: '))

hora_segundo = hora * 3600
minutos_segundos = minuto * 60
segundo_total = hora_segundo + minutos_segundos + segundo

print(f'Se passaram {segundo_total} segundos desde a última meia-noite até a hora lida.')
