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


mostra_sudoku(jogo)
