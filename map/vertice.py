import pygame


class vertice(pygame.sprite.Sprite):
    def __init__(self,pos:tuple,id:int) -> None:
        super().__init__()
        self.id = id
        #self.listaAdjacencia = listaAdjacencia
        self.color = (255, 255, 255)

        self.image = pygame.Surface((20,20), pygame.SRCALPHA)
        pygame.draw.circle(self.image,  self.color, (10,10), 10)
        self.rect = self.image.get_rect(center = pos)

class aresta(pygame.sprite.Sprite):
    def __init__(self,ver1,ver2) -> None:
        super().__init__()
        surface = (abs(ver1.rect.x -  ver2.rect.x )+10,abs(ver1.rect.y  -  ver2.rect.y )+10)
        centro = (((ver1.rect.x +  ver2.rect.x )//2)+10,((ver1.rect.y  +  ver2.rect.y )//2)+10) 
        self.color = (255, 255, 255)

        
        self.image = pygame.Surface(surface, pygame.SRCALPHA)
        pygame.draw.line(self.image,  self.color, (0,0),surface)
        self.rect = self.image.get_rect(center = centro)