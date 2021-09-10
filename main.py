jogo = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def mostra_sudoku(matrix):
    for i in range(len(matrix)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - ')

        for j in range(len(matrix[0])): #iterando pela coluna
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(matrix[i][j])
            else:
                print(f'{matrix[i][j]} ', end="")

def acha_zero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                return (i, j) #linha, coluna

    return None

def numero_eh_valido(matrix, num, pos):
    #linha
    for i in range(len(matrix[0])):
        if matrix[pos[0]][i] == num and pos[1] != i:
            return False

    #coluna
    for i in range(len(matrix)):
        if matrix[i][pos[1]] == num and pos[0] != i:
            return False

    #bloco 9x9
    bloco_x = pos[1] // 3
    bloco_y = pos[0] // 3

    for i in range(bloco_y*3, bloco_y*3 + 3):
        for j in range(bloco_x*3, bloco_x*3 + 3):
            if matrix[i] == num and (i,j) != pos:
                return False

    return True


def resolve_sudoku(matrix):

    achou = acha_zero(matrix)
    if not achou:
        return True #Jogo completo
    else:
        linha, coluna = achou

    for i in range(1, 10): #testa os números de 1 a 9
        if numero_eh_valido(matrix, i, (linha, coluna)):
            matrix[linha][coluna] = i #muda zero para número testado

            if resolve_sudoku(matrix): #Chama a função novamente para continuar preenchendo os zeros
                return True

            #se a função retornou falso significa que o número testado antes foi invalido
            #então volta para a chamada anterior e tenta outro valor

            matrix[linha][coluna] = 0

    return False


mostra_sudoku(jogo)
print("_____________________")
print("                     ")
resolve_sudoku(jogo)
mostra_sudoku(jogo)