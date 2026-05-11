from classes.musica import Musica
from classes.biblioteca import Biblioteca
from classes.fila import Fila

biblioteca = Biblioteca() # instancia as estruturas criadas
playlist_humor = Fila() # fila sem limite
historico = Fila(limite=10) # fila com limite de 10