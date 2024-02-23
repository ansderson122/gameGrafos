import pygame


class vertice(pygame.sprite.Sprite):
    def __init__(self,pos:tuple,id:int) -> None:
        super().__init__()
        self.id = id
        #self.listaAdjacencia = listaAdjacencia
        self.color = (255, 255, 255)

        self.image = pygame.Surface((50,50), pygame.SRCALPHA)
        pygame.draw.circle(self.image,  self.color, (25,25), 10)
        self.rect = self.image.get_rect(center = pos)

