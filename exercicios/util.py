def media(valores):
    return sum(valores) / len(valores)

def gerar_registro(linha):
    registro = linha.split(';')
    return {"nome": registro[0],
            "cidade": registro[1],
            "idade": int(registro[2]),
            "renda": float(registro[3])}

if __name__ == '__main__':
    assert media([1,2,3,4,5]) == 3.0
    print(media([1,2,3,4,5]))

    assert gerar_registro("Jennifer;Aracaju;25;3500") == {"nome": "Jennifer",
                                                          "cidade": "Aracaju",
                                                          "idade": 25,
                                                          "renda": 3500.0}
    print(gerar_registro("Jennifer;Aracaju;25;3500"))
