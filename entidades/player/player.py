import pygame
import os
import math
from entidades import animacao
from entidades.entidade import entidadeAbstrata
from menuLateral.Texto import Texto
from menuLateral.menuLateral import menuLataral

class player(entidadeAbstrata):
    def __init__(self,surface,movimentosRestantes = 100,pos = (250,580)):
       
        self.texto = Texto("",200)
        self.invetario = menuLataral("Inventário",(100,450),"Soltar")

        self.surface = surface
        self.imagens= animacao(self.imagens_idle,pos)
        self.rect = self.imagens.rect

        self.movimentosRestantes = movimentosRestantes 

        self.vida = 100
        self.atk = 30

        self.destino = pos
        self.velocidade = 0.1
        self.idVertici = 1
        self.idVerticiDestino = 0
        self.listAdjacencia = [2,3,4]
        self.novaLista = 0 
        
        super().__init__()
        self.imagensOriginal = []
        self.i =1

    
    @property
    def imagens_idle(self):
        idle = []
        for image in os.listdir("./entidades/player/sprites/idle"):
            carrega = pygame.image.load(f"./entidades/player/sprites/idle/{image}")
            idle.append(carrega)
        return idle
    
    

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
    

    def imagemVermelha(self): 
        if self.dano_ativo:
            return

        self.tempo_inicial = pygame.time.get_ticks()
        self.dano_ativo = True
        imagens = []
        for imagem in self.imagens_idle:
            img = imagem.copy()
            for x in range( img.get_width()):
                for y in range( img.get_height()):
                    cor =  img.get_at((x, y))
                    if cor[3] > 0:  # Verifica se o pixel não é transparente
                        novo_r = min(cor[0] + 150, 255)  # Aumenta o valor do canal vermelho
                        img.set_at((x, y), (novo_r, cor[1], cor[2], cor[3]))  # Define a nova cor

            imagens.append(img)
        self.imagens= animacao(imagens,(self.rect.x,self.rect.y))



    def voltarImagemNormal(self):
        self.dano_ativo = False
        self.imagens= animacao(self.imagens_idle,(self.rect.x,self.rect.y))

    
    def renascer(self):
        self.vida = 100
        
        
    
    def update(self):
        self.imagens.mudar_imagem()
        self.move()
   

        duracao_dano = 500 # Tempo em segundos para manter o efeito que ele esta sendo ataque
        agora = pygame.time.get_ticks()
        if agora > (self.tempo_inicial+duracao_dano) and  self.dano_ativo :
            self.voltarImagemNormal()
            if self.vida <= 0:
                self.renascer()
                        

      
        self.texto.updateTexto(f'Movimentos: {self.movimentosRestantes}')
        self.surface.blit(self.texto.texto,(800,10))

        self.texto.updateTexto(f'Vida: {self.vida}')
        self.surface.blit(self.texto.texto,(600,10))
        self.invetario.update()

        self.surface.blit(self.imagens.imagem, self.rect)   