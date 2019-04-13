"""
variaveis.py

Escreva um programa que execute o trecho de código abaixo e, em seguida, 
imprima o valor e o tipo das variáveis x, y e z ao final da execução. 
""" 

x = 5
y = 7.5
z = x
s = 'exemplo'
x = y + 5
y = z - 1
z = x * 2
t = s
s = y // 2


print('x =', x, type(x))
print('y =', y, type(y))
print('z =', z, type(z))
print('s =', s, type(s))
print('t =', t, type(t))