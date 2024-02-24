import pygame

from menuLateral.Texto import Texto

class Item(pygame.sprite.Sprite):
    def __init__(self,item,atk,dur):
        super().__init__()
        self.item = Texto(item,70,20)
        self.atk = Texto(atk,25,20)
        self.dur = Texto(dur,25,20)


        if item[:3] == "Esp" or item[:3] == "Erv":
            self.tipo = 1
        else:
            self.tipo = 0

        self.numero = 0

        self
