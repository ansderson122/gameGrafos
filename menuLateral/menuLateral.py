from typing import Any
import pygame
from menuLateral.Texto import Texto
from menuLateral.itens import Item

class menuLataral(pygame.sprite.Sprite):
    def __init__(self,texto:str,pos:tuple,ti = "Pegar",num = 1):
        super().__init__()

        self.corFundo = (55,55,55)
        self.ti = ti
    
        self.titulo = Texto(texto, 160)
        self.ultimoPossicao = self.titulo.altura_total + 10
        self.conteudo =  pygame.sprite.Group()
        
        self.image = pygame.Surface((200,300), pygame.SRCALPHA)
        self.image.fill(self.corFundo)
        self.image.blit(self.titulo.texto, (10,10))
        pygame.draw.rect(self.image, (0,0,0), (0, 0,200, 300), 5)
        pygame.draw.line(self.image, (255, 255, 255), (10,  self.ultimoPossicao ), (150,  self.ultimoPossicao ), 2)

        self.cabecario()
        self.rect = self.image.get_rect(center = pos)

        self.numeroBnt = num
        

    def adicionarItem(self,item):
        item1 = Item(item[0],item[1],item[2])
        self.conteudo.add(item1)
        self.update()

    def desenhaItens(self):
        self.ultimoPossicao = self.titulo.altura_total + 35
        numeroBnt =  self.numeroBnt
        for item in self.conteudo:
            self.image.blit(item.item.texto, (50,self.ultimoPossicao))
            self.image.blit(item.atk.texto, (120,self.ultimoPossicao))
            self.image.blit(item.dur.texto, (155,self.ultimoPossicao))

            if item.tipo :
                item.numero = numeroBnt
                texto = Texto(str(numeroBnt), 25,20)
                self.image.blit(texto.texto, (10,self.ultimoPossicao))
                numeroBnt += 1
            self.ultimoPossicao += item.item.altura_total 


    def carregaListaSprints(self):
        lista = []
        for sprit in self.conteudo:
            lista.append(sprit)
        return lista

    def cabecario(self):
        texto = Texto(self.ti,50,20)
        self.image.blit(texto.texto, (10,self.titulo.texto.get_size()[1] +20))

        texto = Texto("item",80,20)
        self.image.blit(texto.texto, (50,self.titulo.texto.get_size()[1] +20))

        texto = Texto("Atk",25,20)
        self.image.blit(texto.texto, (120,self.titulo.texto.get_size()[1] +20))
        
        texto = Texto("Dur",25,20)
        self.image.blit(texto.texto, (155,self.titulo.texto.get_size()[1]))

        self.ultimoPossicao += 20

    def remover_sprite_por_id(self,id_alvo):
        print("não remover_sprite_por_id")

    def update(self):
        self.image.fill(self.corFundo)
        self.image.blit(self.titulo.texto, (10,10))
        pygame.draw.rect(self.image, (0,0,0), (0, 0,200, 300), 5)
        pygame.draw.line(self.image, (255, 255, 255), (10,  self.titulo.texto.get_size()[1] +10 ), (150,  self.titulo.texto.get_size()[1] +10 ), 2)
        
        self.desenhaItens()
        self.cabecario()
