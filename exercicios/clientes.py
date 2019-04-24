import util

arquivo = open('clientes.txt', 'r')
dados = []
for linha in arquivo.readlines():
    registro = util.gerar_registro(linha)
    dados.append(registro)

idades = []
rendas = []
for r in dados:
    idades.append(r['idade'])
    rendas.append(r['renda'])

print('Média de idade:', util.media(idades))
print('Média de renda:', util.media(rendas))
