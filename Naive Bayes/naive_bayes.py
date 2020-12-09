
def classify(treinamento, teste):
    argumentos = {}
    for classe in {elm[-1] for elm in treinamento}:
        count_classe = len([exemplo for exemplo in treinamento if exemplo[-1] == classe])
        argumentos[classe] = count_classe / len(treinamento)
        for i, caracteristica in enumerate(teste):
             argumentos[classe] *= (len([exemplo[i] for exemplo in treinamento if exemplo[-1] == classe and exemplo[i] == caracteristica]) / count_classe)


    l = [(classe,v) for (classe,v) in argumentos.items()]
    l.sort(key=lambda k_v : k_v[1])
    return l[-1][0]


if __name__ == '__main__':

    linhas, colunas = input().rstrip().split()
    linhas = int(linhas)
    colunas = int(colunas)

    treinamento = []
    for l in range(linhas):
        treinamento.append([e for e in input().rstrip().split()])


    teste = [e for e in input().rstrip().split()]
    

    print(classify(treinamento, teste))
