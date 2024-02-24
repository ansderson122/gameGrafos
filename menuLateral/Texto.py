import pygame

class Texto(pygame.sprite.Sprite):
    def __init__(self,texto:str,largura_maxima:int , tamanho_fonte = 35):
        super().__init__()
        self.dadosInicias = (texto,largura_maxima)

        self.corTexto = (255,255,255)
        self.tamanho_fonte = tamanho_fonte
        self.largura_maxima = largura_maxima

        
        font = pygame.font.SysFont("arial", 36)
        self.fonte = pygame.font.Font(None,  self.tamanho_fonte)
        
        self.texto,self.altura_total = self.renderizar_texto(texto, self.largura_maxima)


    def renderizar_texto(self,texto, largura_maxima):
        palavras = texto.split(" ")
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            linha_teste = linha_atual + palavra + " "

            if self.fonte.size(linha_teste)[0] <= largura_maxima:
                linha_atual = linha_teste
            else:
                linhas.append(linha_atual)
                linha_atual = palavra + " "
        
        linhas.append(linha_atual)

        altura_total = len(linhas) * self.tamanho_fonte

        superficie_texto = pygame.Surface((largura_maxima, len(linhas) *  self.tamanho_fonte ), pygame.SRCALPHA)
        for i, linha in enumerate(linhas):
            texto_renderizado = self.fonte.render(linha, True,  self.corTexto)
            superficie_texto.blit(texto_renderizado, (0, i *  self.tamanho_fonte ))

        return superficie_texto,altura_total

    def updateTexto(self,novaTexto):
        self.texto,self.altura_total  = self.renderizar_texto(novaTexto, self.largura_maxima)