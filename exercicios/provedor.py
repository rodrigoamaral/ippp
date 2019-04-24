gb = input('Informe a quantidade de GB consumida: ')
gb = int(gb)
tipo = input('Informe o tipo de plano (R-Residencial, E-Empresarial): ')
valor = 0
if tipo == 'R':
    if gb <= 10:
        valor = 8 * gb
    else:
        valor = (8 * 10) + (12 * (gb - 10))
elif tipo == 'E':
    if gb <= 100:
        valor = 10 * gb
    else:
        valor = (10 * 100) + (15 * (gb - 100))

print('Valor a pagar R$', valor)
    
