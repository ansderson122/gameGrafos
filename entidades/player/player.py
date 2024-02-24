import pygame
import os
import math
from entidades import animacao
from menuLateral.Texto import Texto

class player(pygame.sprite.Sprite):
    def __init__(self,surface,movimentosRestantes = 100,pos = (250,580)):
        super().__init__()

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
    
    def texto(self,texto,pos):
        
        # Definir a cor do texto
        cor_texto = (255, 255, 255)

        # Criar uma instância da classe Font
        fonte = pygame.font.Font(None, 36)  # None usa a fonte padrão do sistema, 36 é o tamanho da fonte

        # Criar um objeto de texto
        texto = fonte.render(texto, True, cor_texto)

        # Posicionar o texto na tela
        posicao_texto = texto.get_rect(center=pos)

        return texto,posicao_texto

    
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

        
        texto, possicao = self.texto(f'Movimentos: {self.movimentosRestantes}',(850,10))
        self.surface.blit(texto,possicao)

        texto, possicao = self.texto(f'Vida: {self.vida}',(600,10))
        self.surface.blit(texto,possicao)

        self.surface.blit(self.imagens.imagem, self.rect)   