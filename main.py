# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from classes import Jogo

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((550, 600))
pygame.display.set_caption('Sudoku')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca

    jogo = Jogo()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados