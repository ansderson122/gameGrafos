import pygame
from sys import exit
from level import level

pygame.init()

tela = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Meu Joquin')
relogio = pygame.time.Clock()
level = level(tela)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar colisão com os vértices
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for vertice in level.vertices.sprites():
                if vertice.rect.collidepoint(mouse_x, mouse_y):
                    level.player.idVerticiDestino = vertice.id
                    level.player.destino = (vertice.rect.x - 10 ,vertice.rect.y-20)
        
        level.get_input()

    level.run()
    
    
    pygame.display.update()
    relogio.tick(60)