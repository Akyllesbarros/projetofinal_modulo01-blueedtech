from personagem import Personagem, personagem
from governo import Governo
from relogio import Relogio
import os
import sys
from time import sleep
from mochila import Mochila
from craft import Foguete, craft





class Menu: 
    def __init__(self) -> None:
        pass


    @staticmethod # Função estática, não preciso atribuir variável, somente chamar a Classe. ( não preciso instanciar objeto nenhum.)
    def apresentacao() :
        os.system('cls')
        input('Pressione ENTER para iniciar o jogo.\n')
        os.system('cls')
        frase1 = 'Desde a praga...'
        frase2 = 'E a mudança de governo... '
        frase3 = 'Esta cidade tem sido insuportável.'
        frase4 = 'Preenchida apenas por Fome, Medo e Controle. '
        frase5 = 'Eu já tentei escapar uma vez, mas falhei...'
        frase6 = 'Mas da próxima vez vai ser diferente.'
        frase7 = 'Eles me chamam de... '
        frase8 = "nome dele em ASCII" 
        frase9 = 'Carta do governo: Acabamos de confiscar seu carro. Obviamente, você não poderá ir muito longe novamente.\nEstamos de olho em você!'
        
                

        for c in frase1 : 
            sys.stdout.flush()
            print(c, end= '') # printa cada letra uma do lado da outra.
            sleep(0.05)
        print('')
        sleep(1)
        for c in frase2 : 
            sys.stdout.flush()
            print(c, end= '') # printa cada letra uma do lado da outra.
            sleep(0.05)
        print('')
        sleep(1)
        for c in frase3 : 
            sys.stdout.flush()
            print(c, end= '') # printa cada letra uma do lado da outra.
            sleep(0.05)
        print('')
        sleep(1)
        for c in frase4 : 
            sys.stdout.flush()
            print(c, end= '') # printa cada letra uma do lado da outra.
            sleep(0.05)
        print('')
        sleep(1)
        for c in frase5 : 
            sys.stdout.flush()
            print(c, end= '') # printa cada letra uma do lado da outra.
            sleep(0.05)
        print('')
        sleep(1)
        for c in frase6 : 
            sys.stdout.flush()
            print(c, end= '') # printa cada letra uma do lado da outra.
            sleep(0.05)
        print('')
        sleep(1)
        for c in frase7 : 
            sys.stdout.flush()
            print(c, end= '') # printa cada letra uma do lado da outra.
            sleep(0.05)
        print('')
        sleep(1)
        os.system('cls')
        for c in frase8 : 
            sys.stdout.flush()
            print(c, end='') # printa cada letra uma do lado da outra.
            sleep(1)
        print('')
        os.system('cls')
        for c in frase9 : 
            sys.stdout.flush()
            print(c, end='') # printa cada letra uma do lado da outra.
            sleep(0.05)
        sleep(1)
        print('')
        os.system('cls')

        print('-------------------------------------------------------- JOGO --------------------------------------------------------')
        frase10 ='''
        A partir de agora, você está sozinho. Mas tem muita terra debaixo da sua casa.
        Use seu sotão para construir um foguete. 
        Cace para comer, mas não saia muito de casa, administre sua energia,
        mas não fique paranóico,
        pois pode ser que as suas ações percam eficiência, 
        mas principalmente...
        Não seja pego pelo governo! 
        '''
        for c in frase10 :
            sys.stdout.flush()
            print(c, end='')
            sleep(0.01)
        input('Aperte ENTER para continuar...\n')
        os.system('cls')
        print('------------------------------------------------ TUTORIAL DO JOGO -------------------------------------------------\n\n')
        print('\n\n[ 1 ] Comer\n[ 2 ] Caçar\n[ 3 ] Construir\n[ 4 ] Dormir\n')
        print('''
        Este é o menu principal. É nele que você poderá es-
        colher suas ações teclando o número correspondente
        de cada item.''')
        input('\nAperte ENTER para continuar o tutorial...\n')
        os.system('cls')
        print('------------------------------------------------ TUTORIAL DO JOGO -------------------------------------------------\n\n')
        print('''
        DICA : Se prepare para o pior.\n\n''')
    
        input('Vamos começar?\n\nAperte ENTER para começar o jogo! ->')
        os.system('cls')

    @staticmethod
    def menuPrincipal(self) :
        menuPrincipal = int(input('\n\n[ 1 ] Comer\n[ 2 ] Caçar\n[ 3 ] Construir\n[ 4 ] Dormir\n\nSelecione uma ação: \n'))

        if menuPrincipal == 1 :
            personagem.comer()
        elif menuPrincipal == 2 :
            personagem.cacar()
        elif menuPrincipal == 3 :
            craft.craft()
        elif menuPrincipal == 4 : 
            personagem.dormir()
