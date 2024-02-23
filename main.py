import pygame
from sys import exit
from map.map import map

pygame.init()
tela = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Meu Joquin')
relogio = pygame.time.Clock()

level = map(tela)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    level.run()
    
    
    pygame.display.update()
    relogio.tick(60)