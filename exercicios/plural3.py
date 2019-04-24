palavras = ['carro', 'melancia', 'balde', 'navio', 'gato', 'floresta']
plurais = [palavra + "s" for i, palavra in enumerate(palavras) if i % 2 != 0]
print(plurais)
