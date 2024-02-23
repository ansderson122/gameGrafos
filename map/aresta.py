import pygame


class aresta(pygame.sprite.Sprite):
    def __init__(self,ver1,ver2) -> None:
        super().__init__()

        # Calcular o centro da linha
        centro_linha = (((ver1.rect.x + ver2.rect.x ) // 2)+10, 
                        ((ver1.rect.y + ver2.rect.y) // 2)+10)

        # Calcular o tamanho da linha
        comprimento_linha = ((ver1.rect.x - ver2.rect.x )**2 + 
                             (ver1.rect.y - ver2.rect.y)**2)**0.5

        self.image = pygame.Surface((comprimento_linha, 2), pygame.SRCALPHA)
        pygame.draw.line(self.image, (255, 255, 255), (0, 0), (comprimento_linha, 0), 2)

        # Calcular o ângulo da linha
        angulo = pygame.math.Vector2(ver1.rect.x - ver2.rect.x , 
                                      ver1.rect.y - ver2.rect.y).angle_to((1, 0))

        # Rotacionar a imagem de acordo com o ângulo
        self.image = pygame.transform.rotate(self.image, angulo)

        self.rect = self.image.get_rect(center=centro_linha)