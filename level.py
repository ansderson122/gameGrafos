import pygame
import json
from map import vertice,aresta
from menuLateral.menuLateral import menuLataral
from entidades import *
import random

class level():
    def __init__(self,surface:pygame.display) -> None:
        self.display_surface = surface

        self.vertices = pygame.sprite.Group()
        self.arestas = pygame.sprite.Group()
        self.menu = pygame.sprite.Group()

        self.informa = menuLataral("Informação do Vértice",(100,150))
        
        self.create_map()

        self.player = player(self.display_surface,self.quatidadeAresta * 3)
        self.crocodilo = crocodilo(self.display_surface)

        self.cerragaMenu()
        self.tempo_ultima_mudanca = pygame.time.get_ticks()
        

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
            
            self.quatidadeAresta = 0
            for chave,listaAdjacencia in self.dados_grafo['edges'].items():
                ver1 = self.procurar_vertice_por_id(int(chave))
                if ver1 == None: continue
                for item in listaAdjacencia:
                    ver2 = self.procurar_vertice_por_id(item)
                    if ver2 == None: continue
                    self.arestas.add(aresta(ver1,ver2))
                    self.quatidadeAresta +=1
            self.quatidadeAresta = self.quatidadeAresta // 2
        except FileNotFoundError:
            print("O arquivo não foi encontrado.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o JSON.")
        except Exception as e:
            print(f"Ocorreu um erro não esperado: {e}")


    def cerragaMenu(self):
        self.menu.empty()
        self.menu.add(self.informa)
        self.menu.add(self.player.invetario)

    def carregaInformacaoVertici(self,id):
        infor = self.dados_grafo["sobre"][f"{id}"] 
        self.informa.update()
        self.informa.conteudo = []
        self.informa.numeroBnt = 1
        self.informa.ultimoPossicao = 80
        for item in infor:
            self.informa.adicionarItem(item)
        self.cerragaMenu()

    def buscaNoVertici(self,num):
        for item in  self.informa.conteudo:
            if item.numero == num:
                return item
        return None
    
    def get_input(self):
        now = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        intervalo_mudanca = 500  # Intervalo de mudança em milissegundos
        con = 0

        
        if  now - self.tempo_ultima_mudanca > intervalo_mudanca:
            self.tempo_ultima_mudanca = now

            if keys[pygame.K_1]:
                for i, elemento in enumerate(self.dados_grafo["sobre"][f'{self.player.idVertici}']):
                    if "Esp" == elemento[0][:3] or elemento[0][:3] == "Erv":
                        con += 1
                    if con == 1:
                        self.player.invetario.adicionarItem(self.dados_grafo["sobre"][f'{self.player.idVertici}'][i])
                        del self.dados_grafo["sobre"][f'{self.player.idVertici}'][i]
                        self.carregaInformacaoVertici(self.player.idVertici)
                        self.player.invetario.update()
                        break  # Parar a iteração após remover a espada

            if keys[pygame.K_2]:
                for i, elemento in enumerate(self.dados_grafo["sobre"][f'{self.player.idVertici}']):
                    if "Esp" == elemento[0][:3] or elemento[0][:3] == "Erv":
                        con += 1
                    if con == 2:
                        self.player.invetario.adicionarItem(self.dados_grafo["sobre"][f'{self.player.idVertici}'][i])
                        del self.dados_grafo["sobre"][f'{self.player.idVertici}'][i]
                        self.carregaInformacaoVertici(self.player.idVertici)
                        self.player.invetario.update()
                        break  # Parar a iteração após remover a espada
            
            if keys[pygame.K_3]:
                for i, elemento in enumerate(self.dados_grafo["sobre"][f'{self.player.idVertici}']):
                    if "Esp" == elemento[0][:3] or elemento[0][:3] == "Erv":
                        con += 1
                    if con == 3:
                        self.player.invetario.adicionarItem(self.dados_grafo["sobre"][f'{self.player.idVertici}'][i])
                        del self.dados_grafo["sobre"][f'{self.player.idVertici}'][i]
                        self.carregaInformacaoVertici(self.player.idVertici)
                        self.player.invetario.update()
                        break  # Parar a iteração após remover a espada

            if keys[pygame.K_6]:
                for i, elemento in enumerate(self.player.invetario.conteudo):
                    if "Esp" == elemento.item.dadosInicias[0][:3] or elemento.item.dadosInicias[0][:3] == "Erv":
                        con += 1

                    if con == 1: 
                        self.dados_grafo["sobre"][f'{self.player.idVertici}'].append([elemento.item.dadosInicias[0],elemento.atk.dadosInicias[0],elemento.dur.dadosInicias[0]])
                        print(self.dados_grafo["sobre"][f'{self.player.idVertici}'])
                        print(self.player.invetario.conteudo)
                        self.player.invetario.conteudo.remove(elemento)
                        print(self.player.invetario.conteudo)

                        self.player.invetario.numeroBnt -= 1
                        self.player.invetario.ultimoPossicao -= elemento.item.texto.get_size()[1]

                        self.carregaInformacaoVertici(self.player.idVertici)
                        self.player.invetario.update()
                        break  # Parar a iteração após remover a espada
            
            if keys[pygame.K_7]:
                for i, elemento in enumerate(self.player.invetario.conteudo):
                    if "Esp" == elemento.item.dadosInicias[0][:3] or elemento.item.dadosInicias[0][:3] == "Erv":
                        con += 1

                    if con == 2:    
                        self.dados_grafo["sobre"][f'{self.player.idVertici}'].append([elemento.item.dadosInicias[0],elemento.atk.dadosInicias[0],elemento.dur.dadosInicias[0]])
                        print(self.dados_grafo["sobre"][f'{self.player.idVertici}'])
                        print(self.player.invetario.conteudo)
                        self.player.invetario.conteudo.remove(elemento)
                        print(self.player.invetario.conteudo)

                        self.player.invetario.numeroBnt -= 1
                        self.player.invetario.ultimoPossicao -= elemento.item.texto.get_size()[1]

                        
                        self.carregaInformacaoVertici(self.player.idVertici)
                        self.player.invetario.update()
                        break  # Parar a iteração após remover a espada
                


            if keys[pygame.K_8]:
                for i, elemento in enumerate(self.player.invetario.conteudo):
                    if "Esp" == elemento.item.dadosInicias[0][:3] or elemento.item.dadosInicias[0][:3] == "Erv":
                        con += 1

                    if con == 3:    
                        self.dados_grafo["sobre"][f'{self.player.idVertici}'].append([elemento.item.dadosInicias[0],elemento.atk.dadosInicias[0],elemento.dur.dadosInicias[0]])
                        print(self.dados_grafo["sobre"][f'{self.player.idVertici}'])
                        print(self.player.invetario.conteudo)
                        self.player.invetario.conteudo.remove(elemento)
                        print(self.player.invetario.conteudo)

                        
                       
                        self.player.invetario.numeroBnt -= 1
                        self.player.invetario.ultimoPossicao -= elemento.item.texto.get_size()[1]
                        self.carregaInformacaoVertici(self.player.idVertici)
                        self.player.invetario.update()
                        break  # Parar a iteração após remover a espada
            
            
 

    def moveMostros(self):
        self.crocodilo.idVerticiDestino = random.choice(self.crocodilo.listAdjacencia)
        ver = self.procurar_vertice_por_id(self.crocodilo.idVerticiDestino)
        self.crocodilo.destino = ((ver.rect.x - 10,ver.rect.y - 30))

    def carregaListaAdjacecia(self):
        if self.player.novaLista: 
            self.player.listAdjacencia = self.dados_grafo['edges'][f'{self.player.idVertici}']
            self.player.novaLista = 0
            self.moveMostros()
            self.carregaInformacaoVertici(self.player.idVertici)
        
        if self.crocodilo.novaLista: 
            self.crocodilo.listAdjacencia = self.dados_grafo['edges'][f'{self.crocodilo.idVertici}']
            ver = self.procurar_vertice_por_id(self.crocodilo.idVertici)
            self.crocodilo.novaLista = 0
            self.crocodilo.rePos((ver.rect.x - 10,ver.rect.y - 30))

    


    def run(self):
        self.display_surface.fill((0,0,0))



        self.vertices.draw(self.display_surface)
        self.arestas.draw(self.display_surface)

        self.menu.draw(self.display_surface)

        self.carregaListaAdjacecia()
        self.player.update()
        self.crocodilo.update()
        #self.click()

        
