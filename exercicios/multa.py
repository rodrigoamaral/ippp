v = input('Informe a velocidade em km/h: ')
v = int(v)
if v > 80:
    print('Você foi multado!')
    valor = (v - 80) * 5
    print('Valor R$ ' + str(valor))
