import os
from classes.musica import Musica
from classes.biblioteca import Biblioteca
from classes.fila import Fila

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') # limpa o terminal para o menu ficar sempre no topo

def main():
    biblioteca = Biblioteca() # instancia as estruturas criadas
    historico = Fila(limite=10) # fila com limite de 10

    relaxar = Fila()  # filas de humor, BPM <= 80
    focar = Fila()    # BPM 81 - 120
    animar = Fila()   # 121 - 160
    treinar = Fila()  # BPM > 160

    while True:
        print('\n' + '='*30)
        print('SISTEMA PLAYLIST')
        print('='*30)
        print('1. Adicionar música à biblioteca')
        print('2. Remover música da biblioteca')
        print('3. Buscar música')
        print('4. Listar biblioteca completa')
        print('5. Montar fila de reprodução por humor')
        print('6. Reproduzir música')
        print('7. Exibir fila de humor')
        print('8. Exibir histórico de reproduções')
        print('9. Estatísticas')
        print('0. Sair')
        print('='*30)

        opcao = input('Digite o número da opção que deseja realizar: ')
        opcoes_validas = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') # tupla para tratar as opções que o usuário pode colocar

        if opcao not in opcoes_validas:
            print('\nOpção inválida. Tente novamente.')

        if opcao == '1':
            print('\n--- CADASTRO DE MÚSICA ---')
            titulo = input('Título: ')
            artista = input('Artista: ')
            genero = input('Gênero: ')
            try:
                bpm = int(input('BPM: ')) # programa tenta converter o que foi digitado em número
                nova_musica = Musica(titulo, artista, genero, bpm) # adiciona música se usuário digitou número
                biblioteca.adicionar_musica(nova_musica)
                print(f'\n Música {titulo} adicionada à Biblioteca')
            except ValueError as e: # só roda se usuário digitar algo que não seja número
                print(f'\n Erro: {e}')

        elif opcao == '2':
            print('\n--- REMOVER MÚSICA ---')
            biblioteca.listar_biblioteca() # apresenta a bilbioteca completa para usuário saber o id
            try:
                id_remover = int(input('\nID da música para remover: '))
                sucesso = biblioteca.remover_musica(id_remover) # remove a música
                if sucesso:
                    print(f' Música {id_remover} removida!')
                else:
                    print(' ID não encontrado.')
            except ValueError:
                print(' Por favor, digite um ID numérico válido.') #erro se digitar algo diferente de número

        elif opcao == '3':
            print('\n--- BUSCAR MÚSICA ---')
            biblioteca.listar_biblioteca() # apresenta a bilbioteca completa para usuário saber o id e título
            termo = input('Digite o ID ou Título da música: ')
            musica_encontrada = biblioteca.buscar_musica(termo) # Retorna o objeto Música se encontrar o id ou título, caso contrário retorna none

            if musica_encontrada:
                print('\nMÚSICA ENCONTRADA:')
                print(musica_encontrada.exibir_dados()) # usa o método exibir_dados() criado em musica.py
                print(f'Gênero: {musica_encontrada.genero}') # exibe o gênero
            else:
                print('\n Música não encontrada na biblioteca.')

        elif opcao == '4':
            print('\n--- BIBLIOTECA COMPLETA ---')
            biblioteca.listar_biblioteca() # apresenta a bilbioteca completa ao usuário

        elif opcao == '5':
            print('\n--- MONTAR PLAYLIST DE HUMOR ---')
            relaxar = Fila() #reseta as filas antigas para montar novamente com a biblioteca atual
            focar = Fila()
            animar = Fila()
            treinar = Fila()

            atual = biblioteca.inicio
            if atual is None:
                print('Biblioteca vazia.') # se a biblioteca estiver vazia
            else:
                while atual is not None: # enquanto a atual não for none (ao chegar no none para, pois chegou ao ultimo elemento)
                    musica = atual.musica # analisa a música atual
                    if musica.bpm <= 80:
                        relaxar.enfileirar(musica)
                    elif musica.bpm >= 81 and musica.bpm <= 120:
                        focar.enfileirar(musica)
                    elif musica.bpm >= 121 and musica.bpm <= 160:
                        animar.enfileirar(musica)
                    else:
                        treinar.enfileirar(musica)
                    atual = atual.proximo # passa o atual para a proxima música
                print('Filas organizadas com sucesso!')

        elif opcao == '6':
            print('\n--- REPRODUZIR MÚSICA ---')
            print('Escolha o humor: 1.Relaxar, 2.Focar, 3.Animar, 4.Treinar')
            vibe = input('Opção: ')
            
            fila_escolhida = None
            if vibe == '1': 
                fila_escolhida = relaxar
            elif vibe == '2': 
                fila_escolhida = focar
            elif vibe == '3': 
                fila_escolhida = animar
            elif vibe == '4': 
                fila_escolhida = treinar

            if fila_escolhida:
                musica_tocando = fila_escolhida.desenfileirar() # retira do topo com dequeue
                if musica_tocando:
                    print(f'\n Tocando agora: {musica_tocando.titulo} - {musica_tocando.artista}')
                    historico.enfileirar(musica_tocando) # enfileira no histórico
                else:
                    print('Fila de humor vazia.') # fila sem músicas
            else:
                print('Opção de humor inválida.') # erro da escolha da opcao 6 (n é número)

        elif opcao == '7':
            print('\n--- EXIBIR FILA DE HUMOR ---')
            print('Escolha: 1.Relaxar, 2.Focar, 3.Animar, 4.Treinar')
            vibe = input('Opção: ')
            if vibe == '1': 
                relaxar.listar_fila()
            elif vibe == '2': 
                focar.listar_fila()
            elif vibe == '3': 
                animar.listar_fila()
            elif vibe == '4': 
                treinar.listar_fila()
            else: 
                print('Opção inválida.')

        elif opcao == '8':
            print('\n--- HISTÓRICO DE REPRODUÇÃO ---')
            historico.listar_fila() # percorre a fila de histórico e lista as músicas

        elif opcao == '9':
            print('\n--- ESTATÍSTICAS ---')
            total_bib = 0 # contagem manual da biblioteca
            atual = biblioteca.inicio
            while atual: # percorre cada nodo da lista
                total_bib += 1 # adc + 1 a cada nodo
                atual = atual.proximo # move para o próximo
            print(f'Total na Biblioteca: {total_bib}') # numero total na biblioteca
            print(f'Fila Relaxar: {relaxar.tamanho}') # quantas possui em cada fila de humor
            print(f'Fila Focar: {focar.tamanho}')
            print(f'Fila Animar: {animar.tamanho}')
            print(f'Fila Treinar: {treinar.tamanho}')
            print(f'Total reproduzidas: {historico.tamanho}') # exibe o histórico

        elif opcao == '0':
            print('\nSistema Encerrado!')
            break

        input('\nPressione Enter para continuar...')
        limpar_tela() # qualquer opção (inválida ou válida) vai cair aqui e limpar o terminal antes de reiniciar o menu

if __name__ == '__main__':
    main() # o programa só inicia se este arquivo for executado diretamente