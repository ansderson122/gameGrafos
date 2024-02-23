import pygame


class animacao(pygame.sprite.Sprite):
    def __init__(self, imagens, posicao_inicial):
        super().__init__()
        self.imagens = imagens
        self.indice_imagem = 0
        self.imagem = self.imagens[self.indice_imagem]
        self.rect = self.imagem.get_rect(midleft=posicao_inicial)
        self.tempo_ultima_mudanca = pygame.time.get_ticks()
        self.intervalo_mudanca = 500  # Intervalo de mudança em milissegundos

    def mudar_imagem(self):
        now = pygame.time.get_ticks()
        if now - self.tempo_ultima_mudanca > self.intervalo_mudanca:
            self.indice_imagem = (self.indice_imagem + 1) % len(self.imagens)
            self.imagem = self.imagens[self.indice_imagem]
            self.tempo_ultima_mudanca = now