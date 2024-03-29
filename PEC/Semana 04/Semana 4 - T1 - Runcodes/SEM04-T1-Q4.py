hora = int(input())
minuto = int(input())
segundo = int(input())

hora_segundo = hora * 3600
minutos_segundos = minuto * 60
segundo_total = hora_segundo + minutos_segundos + segundo

print(f'{segundo_total}')