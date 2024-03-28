import pygame 
import math
import random
from entidades.entidade import entidadeAbstrata

class crocodilo(entidadeAbstrata):
    def __init__(self,surface,pos = (500,300)):
        self.imagem = pygame.image.load("./entidades/crocodilo/crocodile1.png") 
        self.surface = surface

        nova_largura = 50
        nova_altura = 60

        self.imagem = pygame.transform.scale(self.imagem , (nova_largura, nova_altura))
        self.rect = self.imagem.get_rect(midleft=pos)

        self.destino = pos
        self.velocidade = 0.1
        self.idVertici = 14
        self.idVerticiDestino = 14
        self.listAdjacencia = []
        self.novaLista = 1

        self.vida = 100
        self.atk = 30
        
        super().__init__()
