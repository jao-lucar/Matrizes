#Matriz original A = [aij]mXn
#Matriz Transposta T = [aji]nXm


from random import randint

#cria uma matriz de exemplo acordo com i= quantidade de linhas e j= quantidade de colunas
# os campos da matriz são preenchido por numeros aleatórios de 2, a 3

def criar_matriz(i, j=None):
    j = j or i
    return [[randint(2, 3) for _ in range(j)] for _ in range(i)]


# recebe a matriz, que é uma lista multidimencional e exbibe ela de uma forma mais amigavel
def exibir_matriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end='\t')
        print()

# aplica a lógica de matriz composta na matriz que se recebe
def para_trasporta(matriz):
    # a matriz transposta recebe as dimenções de acordo com a lógica dela que é,
    # numero de linhas é o mesmo que o de coluna da original
    # numero de coluna é o mesmo que o de linha da original
    # ela é preenchida por valores nulos antes de receber os verdadeiros
    matrix_trans = [[0 for _ in range(len(matriz))] for _ in range(len(matriz[0]))]

    # estou pegando cada linha da matriz trasnposta e fazendo
    # ela receber uma lista de tamanho igual ao numero de linhas da matriz original
    # cada linha é uma lista em python, e o tamanho das listas corresponde ao numero de colunas da matriz
    # 'i' vai de 0 a quantidade de linhas da matriz transposta
    # 'i' representa cada linha em matriz transposta
    # 'i' representa cada coluna em matriz orinial
    for i in range(len(matrix_trans)):
        matrix_trans[i] = [linha[i] for linha in matriz]

    return matrix_trans


matriz = criar_matriz(2, 4)


exibir_matriz(matriz)
print()
exibir_matriz(para_trasporta(matriz))