import pygame
import math
import random

class entidadeAbstrata(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tempo_inicial = 0
        self.dano_ativo = False
        

    def imagemVermelha(self): 
        if self.dano_ativo:
            return
        
        self.tempo_inicial = pygame.time.get_ticks()
        self.dano_ativo = True
        self.imagensOriginal  =  self.imagem.copy()
        for x in range( self.imagem.get_width()):
            for y in range( self.imagem.get_height()):
                cor =  self.imagem.get_at((x, y))
                if cor[3] > 0:  # Verifica se o pixel não é transparente
                    novo_r = min(cor[0] + 150, 255)  # Aumenta o valor do canal vermelho
                    self.imagem.set_at((x, y), (novo_r, cor[1], cor[2], cor[3]))  # Define a nova cor

    def voltarImagemNormal(self):
        self.dano_ativo = False
        self.imagem = self.imagensOriginal

    def danoRecebido(self,damo):
        self.imagemVermelha()
        self.vida -= damo
       
        
    def renascer(self):
        numero_aleatorio = random.randint(1, 19)

        self.vida = 100
        self.idVertici =  numero_aleatorio
        self.idVerticiDestino =  numero_aleatorio
        self.listAdjacencia = []
        self.novaLista = 1

    
    def rePos(self,pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def move(self):
        if self.idVerticiDestino in self.listAdjacencia:
            # movimentação do player
            self.rect.x += (self.destino[0] - self.rect.x) * self.velocidade 
            self.rect.y += (self.destino[1] - self.rect.y) * self.velocidade 

            margem = 10
            if math.dist((self.rect.x, self.rect.y), self.destino) < margem:
                self.idVertici = self.idVerticiDestino
                self.idVerticiDestino = 0
                self.novaLista = 1
  
    
    def update(self):
        self.move() 
       
        duracao_dano = 500 # Tempo em segundos para manter o efeito que ele esta sendo ataque
        agora = pygame.time.get_ticks()
        if agora > (self.tempo_inicial+duracao_dano) and  self.dano_ativo :
            self.voltarImagemNormal()
            if self.vida <= 0:
                self.renascer()
                        


        self.surface.blit(self.imagem, self.rect)   