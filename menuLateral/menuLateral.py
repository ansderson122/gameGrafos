from typing import Any
import pygame
from menuLateral.Texto import Texto

class menuLataral(pygame.sprite.Sprite):
    def __init__(self,texto:str,pos:tuple):
        super().__init__()

        self.corFundo = (55,55,55)
    
        self.titulo = Texto(texto, 160)
        self.ultimoPossicao = self.titulo.altura_total + 10
        self.conteudo = pygame.sprite.Group()
        
        self.image = pygame.Surface((200,300), pygame.SRCALPHA)
        self.image.fill(self.corFundo)
        self.image.blit(self.titulo.texto, (10,10))
        self.rect = self.image.get_rect(center = pos)


    def adicionarItem(self,item):
        texto = Texto(item, 160)
        self.image.blit(texto.texto, (10,self.ultimoPossicao))
        self.ultimoPossicao += texto.altura_total + 10
        self.conteudo.add(texto)

    def update(self):
        self.image.fill(self.corFundo)
        self.image.blit(self.titulo.texto, (10,10))
