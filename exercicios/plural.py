palavras = ['carro', 'melancia', 'balde', 'navio', 'gato', 'floresta']
plurais = []
for i in range(len(palavras)):
    if i % 2 != 0:
        plurais.append(palavras[i] + "s")
print(plurais)
