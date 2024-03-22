import pygame
import os
import math
from entidades import animacao
from menuLateral.Texto import Texto
from menuLateral.menuLateral import menuLataral

class player(pygame.sprite.Sprite):
    def __init__(self,surface,movimentosRestantes = 100,pos = (250,580)):
        super().__init__()
        self.texto = Texto("",200)
        self.invetario = menuLataral("Inventário",(100,450),"Soltar",6)

        self.surface = surface
        self.imagens= animacao(self.imagens_idle,pos)
        self.rect = self.imagens.rect

        self.movimentosRestantes = movimentosRestantes 
        self.vida = 100

        self.destino = pos
        self.velocidade = 0.1
        self.idVertici = 1
        self.idVerticiDestino = 0
        self.listAdjacencia = [2,3,4]
        self.novaLista = 0

    
    @property
    def imagens_idle(self):
        idle = []
        for image in os.listdir("./entidades/player/sprites/idle"):
            carrega = pygame.image.load(f"./entidades/player/sprites/idle/{image}")
            idle.append(carrega)
        return idle
    
    def get_input(self):
        keys = pygame.key.get_pressed()

    
    def quatidadePossivelTesouro(self):
        # Esse função calcula a quantitade de tesouro que o jogado poede transporta 
        quantidade = 100
        for item in self.invetario.conteudo:
            if item.item.dadosInicias[0][:3] ==  "Esp":
                quantidade -=  int(item.atk.dadosInicias[0]) # menos o atk da espada 
            elif item.item.dadosInicias[0][:3] ==  "Erv":
                quantidade -= 1 # menos uma erva 

        quantidade -= (100 - self.vida)
        return quantidade
    
    
    def update(self):
        self.imagens.mudar_imagem()

        if self.idVerticiDestino in self.listAdjacencia:
            # movimentação do player
            self.rect.x += (self.destino[0] - self.rect.x) * self.velocidade 
            self.rect.y += (self.destino[1] - self.rect.y) * self.velocidade 

            margem = 10
            if math.dist((self.rect.x, self.rect.y), self.destino) < margem:
                self.idVertici = self.idVerticiDestino
                self.idVerticiDestino = 0
                self.novaLista = 1
                self.movimentosRestantes -= 1

        self.texto.updateTexto(f'Movimentos: {self.movimentosRestantes}')
        self.surface.blit(self.texto.texto,(800,10))

        self.texto.updateTexto(f'Vida: {self.vida}')
        self.surface.blit(self.texto.texto,(600,10))
        self.invetario.update()

        self.surface.blit(self.imagens.imagem, self.rect)   