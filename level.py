import pygame
import json
from map import vertice,aresta
from menuLateral.menuLateral import menuLataral
from entidades import player

class level():
    def __init__(self,surface:pygame.display) -> None:
        self.display_surface = surface

        self.vertices = pygame.sprite.Group()
        self.arestas = pygame.sprite.Group()

        self.create_map()
        self.cerragaMenu()

        self.player = player(self.display_surface)
        

    def procurar_vertice_por_id(self, identificador: int):
        for vertice in self.vertices:
            if vertice.id == identificador:
                return vertice
        return None

    def create_map(self):
        try:
            with open('./map/grafo.json', 'r') as arquivo_json:
                self.dados_grafo = json.load(arquivo_json)

            
            for node in self.dados_grafo['nodes']:
                self.vertices.add(vertice(node["pos"],int(node["id"])))
            
            for chave,listaAdjacencia in self.dados_grafo['edges'].items():
                ver1 = self.procurar_vertice_por_id(int(chave))
                if ver1 == None: continue
                for item in listaAdjacencia:
                    ver2 = self.procurar_vertice_por_id(item)
                    if ver2 == None: continue
                    self.arestas.add(aresta(ver1,ver2))

        except FileNotFoundError:
            print("O arquivo não foi encontrado.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o JSON.")
        except Exception as e:
            print(f"Ocorreu um erro não esperado: {e}")


    def cerragaMenu(self):
        self.menu = pygame.sprite.Group()

        self.menu.add(menuLataral("Informação do Vértice",(100,150)))
        self.menu.add(menuLataral("Inventário",(100,450)))

    


    def run(self):
        self.display_surface.fill((0,0,0))


        self.vertices.draw(self.display_surface)
        self.arestas.draw(self.display_surface)

        self.menu.draw(self.display_surface)

        if self.player.novaLista: 
            self.player.listAdjacencia = self.dados_grafo['edges'][f'{self.player.idVertici}']
            self.player.novaLista = 0
            
        self.player.update()
        #self.click()

        
