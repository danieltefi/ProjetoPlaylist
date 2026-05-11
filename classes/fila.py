from typing import Optional
from musica import Musica
from nodos import NodoFila

class Fila: # implementa uma Fila encadeada para playlists e histórico
    
    def __init__(self, limite: Optional[int] = None): # fila precisa saber quem é o primeiro e último para ser rápida
        self.inicio: Optional[NodoFila] = None
        self.fim: Optional[NodoFila] = None
        self.tamanho = 0 # rastreia a quantidade de elementos
        self.limite = limite # define o limite da fila (ex: 10)

    def enfileirar(self, musica: Musica) -> None: # adiciona música ao fim da fila
        if self.limite is not None and self.tamanho >= self.limite: # se atingir o limite, remove a mais antiga antes de inserir
            self.desenfileirar()

        novo_nodo = NodoFila(musica)
        
        if self.fim is None: # se a fila está vazia
            self.inicio = self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo # antigo último aponta para o novo
            self.fim = novo_nodo        # novo nó vira o último da fila

        self.tamanho += 1 # adiciona +1 a contagem de músicas na fila

    def desenfileirar(self) -> Optional[Musica]: # remove e retorna a primeira música da fila (quem entrou primeiro - FIFO)
        if self.inicio is None:
            return None
            
        musica_removida = self.inicio.musica # guarda a música em uma variável temporária antes de desconectar o nó da fila
        self.inicio = self.inicio.proximo # move o início para o segundo da fila
        
        if self.inicio is None: # se a fila ficou vazia após remover
            self.fim = None

        self.tamanho -= 1 # remove -1 a contagem de músicas na fila   
        return musica_removida

    def listar_fila(self) -> None: # exibe os itens da fila sem removê-los
        if self.inicio is None:
            print('Fila vazia.')
            return
            
        atual = self.inicio # começa o percurso pelo primeiro nó da fila
        while atual is not None: # enquanto não chegar ao fim da lista (none)
            print(f'- {atual.musica.titulo} ({atual.musica.artista})')
            atual = atual.proximo # move o ponteiro para o próximo nó