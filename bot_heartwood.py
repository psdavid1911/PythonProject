from random import randrange
from time import sleep
from pyautogui import click, keyDown, keyUp, locateCenterOnScreen, ImageNotFoundException
from keyboard import is_pressed
import cv2


t = 0.4
c = 0.7
t_hold = 0.1
p = 'Imagens_heartwood\\'
class Jogador:


    def __init__(self):
        # posicao inicial do jogador
        try:
            self.posx, self.posy = locateCenterOnScreen(p + 'jogador.png', confidence=c)
            print(f'Posicao do jogador: {self.posx},{self.posy}')
        except ImageNotFoundException: print('Não achei a imagem do jogador')

    def ataca(self):
        click(1700, 800)  # botao de ataque
        click(1800, 655)  # botao habilidade 1
        click(1690, 655)  # botao habilidade 2
        click(1580, 655)  # botao habilidade 3
        click(1550, 740)  # botao habilidade 4
        click(1590, 500)  # botao interacao

    # passo T=0.1 de aprox 85px

    def move_to(self, pos_x, pos_y):
        # delta
        deltax = pos_x - self.posx
        deltay = pos_y - self.posy
        print(f'delta: {deltax},{deltay}')

        # Verifica o quadrante
        setax = 'right' if deltax > 0 else 'left'
        setay = 'down' if deltay > 0 else 'up'
        print(f'movimento: {setax},{setay}')

        deltax = abs(deltax)
        deltay = abs(deltay)

        # caminha
        for passo in range(0, deltax if deltax > deltay else deltay, 85):
            keyDown(setax)
            keyDown(setay)
            sleep(t_hold)
            keyUp(setax)
            keyUp(setay)

        # espera pra tentar dnv
        sleep(5)

    def move_to_life(self):
        print('movendo..')
        try:
            posx, posy = locateCenterOnScreen(p + 'life.png', confidence=c)
            print(f'posicao da vida: {posx},{posy}')
        except ImageNotFoundException:
            print('nao pude encontrar a vida')
        self.move_to(posx, posy)

    def joga(self):
        self.move_to_life()

#Fora da classe
flag = 0
jogador = Jogador()
while True:
    if is_pressed('f1'): flag = 1
    if is_pressed('f2'): flag = 0
    if flag:
        jogador.joga()
        sleep(5)

    # try:
    #     pos = pyautogui.locateCenterOnScreen(p+'aceitar.png', confidence=c)
    #     pyautogui.click(pos.x, pos.y)
    # except pyautogui.ImageNotFoundException:
    #     print('Imagem não encontrada')
    #     time.sleep(t)
    # except KeyboardInterrupt:
    #     print('\n')

# def move():
#     n_aleatorio = randrange(0, 4)
#     direcao = ['left', 'right', 'up', 'down']
#     keyDown(direcao[n_aleatorio])
#     sleep(t_hold)
#     keyUp(direcao[n_aleatorio])
