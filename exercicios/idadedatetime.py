"""
Escreva um programa que peça nome e ano de nascimento do usuário, calcule 
a idade e imprima o resultado no formato abaixo.

'<nome do usuário> tem <idade> anos.'
"""
from datetime import datetime

nome = input('Nome: ')
dia = input('Dia de nascimento: ')
mes = input('Mês de nascimento: ')
ano = input('Ano de nascimento: ')
data_nasc = datetime(int(ano), int(mes), int(dia))
hoje = datetime.today()
idade = hoje.year - data_nasc.year
if hoje.month < data_nasc.month:
    idade -= 1
elif hoje.month == data_nasc.month and hoje.day < data_nasc.day:
    idade -= 1
print(nome, 'tem', idade, 'anos.')