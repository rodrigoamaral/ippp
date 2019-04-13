"""
Escreva um programa que peça nome e ano de nascimento do usuário, calcule 
a idade e imprima o resultado no formato abaixo.

'<nome do usuário> tem <idade> anos.'
"""

nome = input('Nome: ')
ano_nascimento = input('Ano de nascimento: ')
idade = 2019 - int(ano_nascimento)
print(nome, 'tem', idade, 'anos.')