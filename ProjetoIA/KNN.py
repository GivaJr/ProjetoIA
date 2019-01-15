from math import sqrt

avaliacoes = {'Ana':
                  {'Freddy x Jason': 2.5,
                   'O Ultimato Bourne': 3.5,
                   'Star Trek': 3.0,
                   'Exterminador do Futuro': 3.5,
                   'Norbit': 2.5,
                   'Star Wars': 3.0},

              'Marcos':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 3.5,
                   'Star Trek': 1.5,
                   'Exterminador do Futuro': 5.0,
                   'Star Wars': 3.0,
                   'Norbit': 3.5},

              'Pedro':
                  {'Freddy x Jason': 2.5,
                   'O Ultimato Bourne': 3.0,
                   'Exterminador do Futuro': 3.5,
                   'Star Wars': 4.0},

              'Claudia':
                  {'O Ultimato Bourne': 3.5,
                   'Star Trek': 3.0,
                   'Star Wars': 4.5,
                   'Exterminador do Futuro': 4.0,
                   'Norbit': 2.5},

              'Adriano':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 4.0,
                   'Star Trek': 2.0,
                   'Exterminador do Futuro': 3.0,
                   'Star Wars': 3.0,
                   'Norbit': 2.0},

              'Janaina':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 4.0,
                   'Star Wars': 3.0,
                   'Exterminador do Futuro': 5.0,
                   'Norbit': 3.5},

              'Leonardo':
                  {'O Ultimato Bourne': 4.5,
                   'Norbit': 1.0,
                   'Exterminador do Futuro': 4.0}
              }


def euclidiana(user1, user2):
    s1 = {}
    for item in avaliacoes[user1]:
        if item in avaliacoes[user2]: s1[item] = 1

    if len(s1) == 0: return 0

    soma = sum([pow(avaliacoes[user1][item] - avaliacoes[user2][item], 2)
                for item in avaliacoes[user1] if item in avaliacoes[user2]])
    return 1/(1 + sqrt(soma))


def manhattan(user1,  user2):
    s1 = {}
    for item in avaliacoes[user1]:
        if item in avaliacoes[user2]: s1[item] = 1

    if len(s1) == 0: return 0

    soma = sum([(avaliacoes[user1][item] - avaliacoes[user2][item])
                for item in avaliacoes[user1] if item in avaliacoes[user2]])
    return 1 / (1 + (soma))


def cosseno(user1, user2):
    s1 = {}
    for item in avaliacoes[user1]:
        if item in avaliacoes[user2]: s1[item] = 1

    if len(s1) == 0: return 0

    numerador = (avaliacoes[user1][item] * avaliacoes[user2][item])

    denominadorA = 0
    denominadorA +=sum([pow(avaliacoes[user1][item], 2)
                for item in avaliacoes[user1] if item in avaliacoes[user2]])
    denominadorB = 0
    denominadorB +=sum([pow(avaliacoes[user2][item], 2)
                for item in avaliacoes[user1] if item in avaliacoes[user2]])
    denominador = denominadorA*denominadorB

    return (numerador/denominador)





def getSimilares(user):
    similaridade = [(euclidiana(user, otherUser), otherUser)
                    for otherUser in avaliacoes if otherUser != user]

    #similaridade = [(manhattan(user, otherUser), otherUser)
    #                for otherUser in avaliacoes if otherUser != user]
    #similaridade = [(cosseno(user, otherUser), otherUser)
    #                 for otherUser in avaliacoes if otherUser != user]


    similaridade.sort()
    similaridade.reverse()
    return similaridade


def getRecomendacoes(user):
    totais={}
    somaSimilaridade={}
    for outro in avaliacoes:
        if outro == user: continue
        similaridade = euclidiana(user, outro)
        #similaridade = manhattan(user, outro)
        #similaridade = cosseno(user,outro)

        if similaridade <= 0: continue

        for item in avaliacoes[outro]:
            if item not in avaliacoes[user]:
                totais.setdefault(item, 0)
                totais[item] += avaliacoes[outro][item] * similaridade
                somaSimilaridade.setdefault(item,0)
                somaSimilaridade[item] += similaridade

    rankings=[(total / somaSimilaridade[item], item) for item, total in totais.items() ]
    rankings.sort()
    rankings.reverse()
    return rankings


def carregaDataBase(path= '/Users/giva/Downloads/ml-100k'):
    filmes = {}
    for linha in open(path + '/u.item'):
        (id, titulo) = linha.split('|')[0:2]
        filmes[id] = titulo

    # print(filmes)



