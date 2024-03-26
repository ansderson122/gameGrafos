import pygame 
import math
import random

class crocodilo(pygame.sprite.Sprite):
    def __init__(self,surface,pos = (500,300)):
        super().__init__()

        self.surface = surface
        self.imagem = pygame.image.load("./entidades/crocodilo/crocodile1.png") 
        largura_original, altura_original = self.imagem.get_size()

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

    def rePos(self,pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    
    def update(self):
        if self.idVerticiDestino in self.listAdjacencia:
            # movimentação do player
            self.rect.x += (self.destino[0] - self.rect.x) * self.velocidade 
            self.rect.y += (self.destino[1] - self.rect.y) * self.velocidade 

            margem = 10
            if math.dist((self.rect.x, self.rect.y), self.destino) < margem:
                self.idVertici = self.idVerticiDestino
                self.idVerticiDestino = 0
                self.novaLista = 1

                        


        self.surface.blit(self.imagem, self.rect)   