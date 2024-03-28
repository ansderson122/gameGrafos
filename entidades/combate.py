import pygame
from menuLateral.Texto import Texto

class Combate:
    def __init__(self) -> None:
        self.listCombate = []
        self.contraAtk = []

    def adicionaCombate(self, combatente1 , combatenten2):
        self.listCombate.append([combatente1,combatenten2,0]) # o terceiro parametro é o turno 


    def combate(self,armasPlayer,event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        agora = pygame.time.get_ticks()

        for combate in self.listCombate:
            atacou = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for item in armasPlayer:
                    if item.rect.collidepoint(mouse_x, mouse_y) and not atacou:
                        atkTotal = int(item.atk.dadosInicias[0]) + combate[0].atk
                        atacou = True
               
                        dur = int(item.dur.dadosInicias[0]) - 1
                        if dur == 0:
                            combate[0].invetario.conteudo.remove(item)
                        else:
                            item.dur = Texto(str(dur),25,20)

                        combate[1].danoRecebido(atkTotal)
                        
        
                if combate[1].rect.collidepoint(mouse_x, mouse_y) :
                    atacou = True
                    combate[1].danoRecebido(combate[0].atk)

                if atacou:
                    combate[2] += 1
                    self.contraAtk.append([combate[0],combate[1],agora + 500])

    def contraAtaque(self):
        agora = pygame.time.get_ticks()

        contraAtk = self.contraAtk
        for combate in contraAtk:
            if combate[2] <  agora:
                combate[0].danoRecebido(combate[1].atk)
                self.contraAtk.remove(combate)
          
            
    def update(self,armasPlayer = None,evento= None):
        self.combate(armasPlayer,evento)
