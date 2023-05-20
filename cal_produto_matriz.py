# para calcular o produto de uma matriz é preciso que as matrizes sejam capazes
# o numero de colunas de A deve ser igual ao numero de linhas de B e o produto que é o C
# possuirá a dimenção cujo a quantidade de linhas é de A e coluna de B
# para ter o produto a gente multiplica as linhas de A pelas colunas de B
# o primeiro termo de C, ou seja, C[c00], é igual ao somatório das multiplicacões
# da primeira linha de A pela primeiro coluna de B
from random import randint


# cria uma matriz de exemplo acordo com i= quantidade de linhas e j= quantidade de colunas
# os campos da matriz são preenchido por numeros aleatórios de 2, a 3
# se for concedido somente um valor das dimenções da matriz, isso quer dizer que é uma matriz quadrada
# então linha é igual a coluna
def create_matriz(i, j=None):
    j = j or i
    matriz = [[randint(2, 9) for _ in range(j)] for _ in range(i)]
    return matriz


# recebe a matriz, que é uma lista multidimencional e exbibe ela de uma forma mais amigavel
def exibir_matriz(matriz):
    for x in matriz:
        for y in x:
            print(y, end='\t\t')
        print()


def produto_matriz(matriz_A, matriz_B):
    # a matriz produto recebe as dimenções de acordo com a lógica dela que é,
    # o numero de linhas de A e colunas de B
    # ela é preenchida por valores nulos antes de receber os verdadeiros
    matriz_C = [[0 for _ in range(len(matriz_B[0]))] for _ in range(len(matriz_A))]

    for i, _ in enumerate(matriz_C):  # para cada linha em matriz C(produto) i=linha
        for j, _ in enumerate(matriz_C[0]):  # para cada coluna em matriz C(produto): j=coluna
            somatorio = []
            for k in range(len(matriz_A[0])): # k= indice do somatorio, ele serve pra percorrer as colunas de A e
                # linhas de B (k pode ir ate o tamaho de coluna de A ou linha de B, no caso ele é do tamanho de
                # coluna de A)
                somatorio.append(matriz_A[i][k] * matriz_B[k][j])
            matriz_C[i][j] = sum(somatorio)

    return matriz_C


matriz_A = create_matriz(3)
matriz_B = create_matriz(3, 4)
exibir_matriz(matriz_A)
print()
exibir_matriz(matriz_B)
print()
exibir_matriz(produto_matriz(matriz_A, matriz_B))
