from typing import Optional
from musica import Musica
from nodos import NodoLista

class Biblioteca: # gerencia a biblioteca de músicas usando lista encadeada simples

    def __init__(self): # biblioteca começa vazia, então o início aponta para none
        self.inicio: Optional[NodoLista] = None

    def popular_biblioteca(self): # adiciona músicas predefinidas para facilitar os testes do sistema
        
        dados_iniciais = [
            ("Lofi Study", "Lofi Girl", "Lofi", 70),       # Relaxar
            ("Fix You", "Coldplay", "Pop", 121),           # Animar
            ("Master of Puppets", "Metallica", "Metal", 212), # Treinar
            ("Stay", "The Kid LAROI", "Pop", 85)           # Focar
        ]
        
        for titulo, artista, genero, bpm in dados_iniciais:
            self.adicionar_musica(Musica(titulo, artista, genero, bpm)) # adiciona as musicas testes na biblioteca

    def adicionar_musica(self, musica: Musica) -> None: # insere uma música no final da lista
                                                        # -> None: usado para indicar que a função não retorna nenhum valor

        novo_nodo = NodoLista(musica) # encapsula o objeto musica em um nó para que ele possa ser inserido na lista encadeada

        if self.inicio is None: # se não há ninguém, a nova música vira o início
            self.inicio = novo_nodo
        else: # caso contrário, percorremos até o último nó
            atual = self.inicio
            while atual.proximo is not None: # continua enquanto houver um próximo
                atual = atual.proximo
            
            atual.proximo = novo_nodo # chega no ultimo e aponta para o novo nó

    def listar_biblioteca(self) -> None: # percorre e exibe as músicas cadastradas

        if self.inicio is None:
            print('\nA biblioteca está vazia.')
            return

        print('\n--- BIBLIOTECA COMPLETA ---')
        atual = self.inicio
        while atual is not None: # percorre do início ao fim
            print(atual.musica.exibir_dados()) # chama o método criado no musica.py
            print('-' * 30)
            atual = atual.proximo # move para o próximo nó

    def remover_musica(self, id: int) -> bool: # busca pelo id e remove o nó correspondente
                                           # -> bool: espera uma saída com valor booleano (true ou false)
                                           # true se removeu, false se não encontrou
                                           

        if self.inicio is None:
            return False # lista vazia, nada para remover

        if self.inicio.musica.id == id: # quando a música removida é a primeira da lista
            self.inicio = self.inicio.proximo # início passa a ser o segundo nó
            return True

        # ponteiros para percorrer a lista na busca do id
        anterior = self.inicio # fica um passo atrás para manter a conexão da lista
        atual = self.inicio.proximo # é o nó que está sendo testado para ver se o id coincide

        while atual is not None:
            if atual.musica.id == id: # verifica se a música dentro do nó atual é a desejada para remover
                anterior.proximo = atual.proximo # nó anterior passa a apontar para o que vem depois do atual
                return True
            
            anterior = atual # anterior assume a posição do atual
            atual = atual.proximo # atual pula para o próximo nó da lista

        return False # percorreu tudo e não achou o id

    def buscar_musica(self, termo: str) -> Optional[Musica]: # busca por id ou título, retorna a música
                                                         # -> Optional[Musica]: pode retornar uma música ou none

        if self.inicio is None:
            return None # biblioteca vazia

        atual = self.inicio
        while atual is not None: # percorre a lista do início ao fim
                                 # verifica se o termo coincide com id (convertido para string) ou com título 
            if str(atual.musica.id) == termo or atual.musica.titulo.lower() == termo.lower(): # lower padroniza para minúsculas
                return atual.musica # retorna o objeto musica 
            
            atual = atual.proximo # avança para o próximo nó

        return None # percorreu tudo e não encontrou nada