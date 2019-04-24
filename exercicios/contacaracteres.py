frase = input('Digite uma frase: ')
contagem = {}
for c in frase:
    if not c in contagem:
        contagem[c] = 0
    contagem[c] += 1
print(contagem)
    
