import pygame
import os
from entidades import animacao

class player(pygame.sprite.Sprite):
    def __init__(self,surface):
        super().__init__()

        self.surface = surface
        self.imagens= animacao(self.imagens_idle,(250,580))
        self.rect = self.imagens.rect

    
    @property
    def imagens_idle(self):
        idle = []
        for image in os.listdir("./entidades/player/sprites/idle"):
            carrega = pygame.image.load(f"./entidades/player/sprites/idle/{image}")
            idle.append(carrega)
        return idle
    
    
    
    def update(self):
        self.imagens.mudar_imagem()
        self.surface.blit(self.imagens.imagem, self.rect)   