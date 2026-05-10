class Musica: # atributo de classe, representa uma faixa musical
    proximo_id_disponivel = 1 # garante id sequencial e único

    def __init__(self, titulo: str, artista: str, genero: str, bpm: int):
        self.id = Musica.proximo_id_disponivel # atribui o id atual e incrementa o contador da classe
        Musica.proximo_id_disponivel += 1
        
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        
        if not isinstance(bpm, int) or bpm <= 0: # isinstance verifica se a variável pertence ao determinado tipo de dado (int)
            raise ValueError('BPM deve ser um número inteiro maior que zero.') # se o valor de bpm não for um número int
        self.bpm = bpm

    def exibir_dados(self) -> str: # retorna string formatada para o menu
        return f'ID: {self.id} \nMúsica: {self.titulo} - {self.artista} \nBPM: {self.bpm}'