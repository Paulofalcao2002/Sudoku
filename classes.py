import pygame


class Quadrado:
    def __init__(self, x, y, valor, janela):
        self.x = x
        self.y = y
        self.valor = valor
        self.width = 50
        self.height = 50
        self.tentativa = 0
        pygame.draw.rect(janela, (0, 0, 0), (self.x, self.y, 50, 50), 3)

class Jogo:
    def __init__(self, codigo, janela):
        self.codigo = codigo
        self.janela = janela
        self.jogo = [
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
        self.quadrados = []
        self.cordenadas = [50, 100, 150, 200, 250, 300, 350, 400, 450]

    def addQuadrado(self):
        for i, linha in enumerate(self.jogo):
            for j, valor in enumerate(linha):
                self.quadrados.append(Quadrado(self.cordenadas[j], self.cordenadas[i], valor, self.janela))







