import time

# Obtém a quantidade de tempo de acordo com as entradas do usuário
horas = int(input('Quantas horas até o seu alarme?\n'))
minutos = int(input('Quantos minutos?\n'))
segundos = int(input('Quantos segundos?\n'))

horas_em_segundos = horas * 60 * 60
minutos_em_segundos = minutos * 60

tempo_total = horas_em_segundos + minutos_em_segundos + segundos

# Aguarda o tempo informado antes de imprimir a mensagem
time.sleep(tempo_total)
print('Temporizador ativado!')
