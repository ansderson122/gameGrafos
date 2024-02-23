import pygame
from menuLateral.Texto import Texto

class menuLataral(pygame.sprite.Sprite):
    def __init__(self,texto:str,pos:tuple):
        super().__init__()

        self.corFundo = (55,55,55)
    
        titulo = Texto(texto, 160)
        
        self.image = pygame.Surface((200,300), pygame.SRCALPHA)
        self.image.fill(self.corFundo)
        self.image.blit(titulo.texto, (10,10))
        self.rect = self.image.get_rect(center = pos)
