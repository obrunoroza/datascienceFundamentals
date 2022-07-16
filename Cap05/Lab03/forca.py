# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
from random import randint
from os import system
from sys import platform
from time import sleep

# Board (tabuleiro)
tabuleiro: list = ['''
>>>>>>>>>> Forca <<<<<<<<<<

 +---+
 |   |
     |
     |
     |
     |
=========''', '''
>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''
>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''
>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
>>>>>>>>>> Forca <<<<<<<<<<
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe do jogo
class Forca(object):

    # Metodo construtor
    def __init__(self, palavra: str) -> None:
        self.__palavra: str = palavra
        self.__letras_certas: list = []
        self.__letras_erradas: list = []

    @property
    def get_palavra(self):
        return self.__palavra

    # Metodo para verificar se a letra está na palavra
    def verifica_letra(self, letra: str) -> bool:
        if letra in self.__palavra and letra not in self.__letras_certas:
            self.__letras_certas.append(letra)
        elif letra not in self.__palavra and letra not in self.__letras_erradas:
            self.__letras_erradas.append(letra)
        else:
            return False
        return True

    # Metodo para verificar se o jogador venceu, ou se acabou as tentativas
    def fim_de_jogo(self) -> bool:
        return self.venceu() or (len(self.__letras_erradas) == 6)

    # Metodo verifica se não existe underline na palavra
    def venceu(self) -> bool:
        if "_" not in self.mostra_palavra():
            return True
        return False

    # Metodo de exibição da palavra
    def mostra_palavra(self) -> str:
        exibe: str = ''
        for letra in self.__palavra:
            if letra not in self.__letras_certas:
                exibe += '_'
            else:
                exibe += letra
        return exibe

    # Metodo para verificar o estado atual do jogo
    def estado_do_jogo(self) -> None:
        if platform == 'windows':
            system('cls')
        else:
            system('clear')

        print(tabuleiro[len(self.__letras_erradas)])
        print(f'\nPalavra: {self.mostra_palavra()}')
        print(f'\nLetras certas: ', end='')
        for letra in self.__letras_certas:
            print(letra, end=', ')

        print(f'\nLetras erradas: ', end='')
        for letra in self.__letras_erradas:
            print(letra, end=', ')


# Função que gera a palavra de forma aleatoria
def gera_palavra() -> str:
    with open('palavras.txt', mode='r') as arquivo:
        cofre = arquivo.readlines()
        return cofre[randint(0, len(cofre))].strip()


# função principal
def main():

    jogo = Forca(gera_palavra())

    while not jogo.fim_de_jogo():
        jogo.estado_do_jogo()
        letra = input("\nDigite uma letra: ")
        jogo.verifica_letra(letra)

    jogo.estado_do_jogo()

    if jogo.venceu():
        print()
        print('\nParabéns você venceu!!')
        sleep(2)
    else:
        print()
        print('\nFim de jogo, você perdeu!!')
        print(f"A palavra era '{jogo.get_palavra}'")
        sleep(2)


if __name__ == '__main__':
    main()

