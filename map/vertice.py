import pygame


class vertice(pygame.sprite.Sprite):
    def __init__(self,pos:tuple,id:int) -> None:
        super().__init__()
        self.possicao = pos
        self.id = id
        #self.listaAdjacencia = listaAdjacencia
        self.color = (255, 255, 255)

        self.image = pygame.Surface((20,20), pygame.SRCALPHA)
        pygame.draw.circle(self.image,  self.color, (10,10), 10)
        self.rect = self.image.get_rect(center = self.possicao)
    
class aresta(pygame.sprite.Sprite):
    def __init__(self,ver1,ver2) -> None:
        super().__init__()
        surface = (abs(ver1.possicao[0] -  ver2.possicao[0]),abs(ver1.possicao[1] -  ver2.possicao[1]))
        centro = (surface[0]//2,surface[1]//2) 

        self.image = pygame.Surface(surface, pygame.SRCALPHA)
        pygame.draw.line(self.image,  self.color, (0,0),surface)
        self.rect = self.image.get_rect(center = centro)
    
  