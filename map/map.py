import pygame
import json
from map.vertice import vertice,aresta

class map():
    def __init__(self,surface:pygame.display) -> None:
        self.display_surface = surface
        self.create_map()

    def procurar_vertice_por_id(self, identificador: int):
        for vertice in self.grid:
            if vertice.id == identificador:
                return vertice
        return None

    def create_map(self):
        self.grid = pygame.sprite.Group()

        with open('./map/grafo.json', 'r') as arquivo_json:
            self.dados_grafo = json.load(arquivo_json)

        for node in self.dados_grafo['nodes']:
            self.grid.add(vertice(node["pos"],self.node["id"]))
          
        for edge in self.dados_grafo['edges']:

            self.grid.add(aresta()

    def run(self):
        self.grid.draw(self.display_surface)
