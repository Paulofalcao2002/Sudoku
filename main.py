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
    window.fill((255, 255, 255))  # Preenche com a cor branca
    jogo = Jogo(1, window)
    jogo.addQuadrado()

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            # get a list of all sprites that are under the mouse cursor
            clicked_sprites = [s for s in jogo.quadrados if s.rect.collidepoint(pos)]
            for sprite in clicked_sprites:
                print(sprite.x, sprite.y)

    # ----- Gera saídas




    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados