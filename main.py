

vermelho = '\033[31m'
verde = '\033[32m'
amerelo = '\033[33m'
branco = '\033[30m'


lista1 = [
    [2,4,5],
    [5,4,57],
    [2,90,5],
]

lista2 = [
    [2,4,5],
    [2,4,60],
    [2,4,5],
]

bigMatrix = []

bigMatrix.append(lista1)
bigMatrix.append(lista2)

def verificador(item):
    lascado = vermelho + 'Lascado'
    perigo = amerelo + 'Em perigo'
    inteiro = verde + 'Inteiro'
    if item > 80:
        print(lascado)
    elif item > 50:
        print(perigo)
    else:
        print(inteiro)

    

def forEach(array, function):
    for item in array:
        function(item)

def read(array):

    # use o map para listar
    for item in array:
            for smallItem in item:
                verificador(smallItem)
    print(branco)



forEach(bigMatrix, read)