import pygame
import json
from map import vertice,aresta
from menuLateral.menuLateral import menuLataral
from menuLateral.Texto import Texto
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
        self.informa.conteudo.empty()
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
    

    
    def verificar_tesouro_e_posicao(self):
        # verifica se ha tesouro no vertice do player 
        # se houve retorna tambem a possiçao 
        for i, sublist in enumerate(self.dados_grafo["sobre"][f'{self.player.idVertici}']):
            if "Tesouro" in sublist:
                return True, i
        return False, None


    
    def perdeTesouro(self):
        quantidadeDoPlayer = self.player.quatidadePossivelTesouro()

        for i,item in enumerate(self.player.invetario.conteudo):
            if item.item.dadosInicias[0] == 'Tesouro':
                if int(item.atk.dadosInicias[0]) > quantidadeDoPlayer:
                    resto = int(item.atk.dadosInicias[0]) - quantidadeDoPlayer

                    self.player.invetario.carregaListaSprints()[i].atk = Texto(str(quantidadeDoPlayer),25,20)
       
                    v,possicao = self.verificar_tesouro_e_posicao()
                    if v:
                        quantidadeVerticeTesouro = int(self.dados_grafo["sobre"][f'{self.player.idVertici}'][possicao][1])
                        self.dados_grafo["sobre"][f'{self.player.idVertici}'][possicao][1] = str(quantidadeVerticeTesouro + resto)

                        
                    else:
                        self.dados_grafo["sobre"][f'{self.player.idVertici}'].append([item.item.dadosInicias[0],str(resto),item.dur.dadosInicias[0]])

                   
    def  verificar_tesouro_e_posicao_player(self):
        # verifica se ha tesouro no player 
        # se houve retorna tambem a possiçao 
        for i, sublist in enumerate(self.player.invetario.conteudo):
            if "Tesouro" == sublist.item.dadosInicias[0]:
                return True, i
        return False, None


    
    def pegarItemVertice(self,possicao):
        # O possicao é a possiçao do item dentro da lista 
        if len(self.dados_grafo["sobre"][f'{self.player.idVertici}']) < possicao + 1:
            return

        item = self.dados_grafo["sobre"][f'{self.player.idVertici}'][possicao]

        if item[0] == "Tesouro":
            quantidadeVertice = int(item[1])
            quantidadeDoPlayer = self.player.quatidadePossivelTesouro()
            restoTesouro =  quantidadeVertice - quantidadeDoPlayer


            if quantidadeDoPlayer >  quantidadeVertice:
                item[1] = str(quantidadeVertice) # quantidade do vertice
            else:
                item[1] = str(quantidadeDoPlayer) # quantidade que ele pode carrega 
            
            v,pos = self.verificar_tesouro_e_posicao_player()
            if v:
                num = int(self.player.invetario.carregaListaSprints()[pos].atk.dadosInicias[0])
                self.player.invetario.carregaListaSprints()[pos].atk = Texto(str(int(item[1]) + num),25,20)
            else: 
                self.player.invetario.adicionarItem(item)
            

            if restoTesouro > 0:
                self.dados_grafo["sobre"][f'{self.player.idVertici}'][possicao][1] = str(restoTesouro)
            else:
                del self.dados_grafo["sobre"][f'{self.player.idVertici}'][possicao]
        else:
            self.player.invetario.adicionarItem(item)
            del self.dados_grafo["sobre"][f'{self.player.idVertici}'][possicao]

        self.perdeTesouro()
        self.carregaInformacaoVertici(self.player.idVertici)
        self.player.invetario.update()
        

    def soltarItemVertice(self,possicao):
        if len(self.player.invetario.conteudo) < possicao + 1:
            return

        item = self.player.invetario.carregaListaSprints()[possicao]

        if item.item.dadosInicias[0]  == "Tesouro":
            quantidade = int(item.atk.dadosInicias[0])

            self.player.invetario.conteudo.remove(item)

            v,pos = self.verificar_tesouro_e_posicao()
            if v:
                print(self.dados_grafo["sobre"][f'{self.player.idVertici}'][pos][1],v)
                quantidadeVerticeTesouro = int(self.dados_grafo["sobre"][f'{self.player.idVertici}'][pos][1])
                self.dados_grafo["sobre"][f'{self.player.idVertici}'][pos][1] = str(quantidadeVerticeTesouro + quantidade)
            else:
                self.dados_grafo["sobre"][f'{self.player.idVertici}'].append([item.item.dadosInicias[0],str(quantidade),item.dur.dadosInicias[0]])

        else:
            self.dados_grafo["sobre"][f'{self.player.idVertici}'].append([item.item.dadosInicias[0],item.atk.dadosInicias[0],item.dur.dadosInicias[0]])
            self.player.invetario.conteudo.remove(item)


        self.carregaInformacaoVertici(self.player.idVertici)
        self.player.invetario.update()
            

    
    def eventos(self,event):
        now = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        intervalo_mudanca = 500  # Intervalo de mudança em milissegundos


        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar colisão com os vértices
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for vertice in self.vertices.sprites():
                if vertice.rect.collidepoint(mouse_x, mouse_y):
                    self.player.idVerticiDestino = vertice.id
                    self.player.destino = (vertice.rect.x - 10 ,vertice.rect.y-20)
        

        
        if  now - self.tempo_ultima_mudanca > intervalo_mudanca:
            self.tempo_ultima_mudanca = now

            if keys[pygame.K_1]:
                self.pegarItemVertice(1)

            elif keys[pygame.K_2]:
               self.pegarItemVertice(2)
            
            elif keys[pygame.K_3]:
                self.pegarItemVertice(3)

            elif keys[pygame.K_6]:
                self.soltarItemVertice(0)
            
            elif keys[pygame.K_7]:
                self.soltarItemVertice(1)
                
            elif keys[pygame.K_8]:
               self.soltarItemVertice(2)
            
 

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

        
