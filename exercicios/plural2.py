palavras = ['carro', 'melancia', 'balde', 'navio', 'gato', 'floresta']
plurais = []
for i, palavra in enumerate(palavras):
    if i % 2 != 0:
        plurais.append(palavra + "s")
print(plurais)
