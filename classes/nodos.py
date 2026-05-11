from musica import Musica # importa a classe Musica
from typing import Optional

class NodoLista: # nó para lista encadeada simples da biblioteca.
    def __init__(self, musica: Musica):
        self.musica = musica # o 'dado' do nó é um objeto Musica
        self.proximo: Optional['NodoLista'] = None # referência para o próximo nó
                                                   # optional é usado como sinalizador de "fim de linha"
                                                   # se o próximo for None, sabe-se que chegou-se ao último elemento da biblioteca ou fila
                                                   # ['NodoLista']: entre aspas pois na definição do atributo proximo a classe não terminou de ser criada ainda
                                                   # ' ' avisa para esperar a definição terminar antes de validar o tipo

class NodoFila: # nó encadeado usado internamente pela fila FIFO
    def __init__(self, musica: Musica):
        self.musica = musica # o 'dado' do nó
        self.proximo: Optional['NodoFila'] = None # referência para o próximo