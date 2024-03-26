import pygame

class Combate:
    def __init__(self) -> None:
        self.listCombate = []

    def adicionaCombate(self, combatente1 , combatenten2):
        self.listCombate.append([combatente1,combatenten2,0]) # o terceiro parametro é o turno 

    def imegemVermelha(self,entidade):
        for x in range(entidade.imagem.get_width()):
                for y in range(entidade.imagem.get_height()):
                    cor = entidade.imagem.get_at((x, y))
                    if cor[3] > 0:  # Verifica se o pixel não é transparente
                        novo_r = min(cor[0] + 150, 255)  # Aumenta o valor do canal vermelho
                        entidade.imagem.set_at((x, y), (novo_r, cor[1], cor[2], cor[3]))  # Define a nova cor
                    
    def combate(self,armasPlayer,event):
        mouse_x, mouse_y = pygame.mouse.get_pos()


        for combate in self.listCombate:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for item in armasPlayer:
                    if item.rect.collidepoint(mouse_x, mouse_y):
                        print("ok")
                        
                
                if combate[1].rect.collidepoint(mouse_x, mouse_y):
                    self.imegemVermelha(combate[1])
        
                    print("ok")
                
                combate[1].imagem.fill((255,255,255))

                    
                    
            

    def update(self,armasPlayer = None,evento= None):
        self.combate(armasPlayer,evento)