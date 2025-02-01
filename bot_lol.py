# Foi preciso instalar o opencv
# Dica:
# import cv2 # nesse ponto a IDE sugere a instalação do pacote opencv-python
import pyautogui, time

t = 0.4
c = 0.9
p = 'Imagens_lol\\'
while True:
    try:
        pos = pyautogui.locateCenterOnScreen(p+'aceitar.png', confidence=c)
        pyautogui.click(pos.x, pos.y)
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada')
        time.sleep(t)
    try:
        pos = pyautogui.locateCenterOnScreen(p+'ranq.png', confidence=c)
        pyautogui.click(pos.x, pos.y)
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada')
        time.sleep(t)
    try:
        pos = pyautogui.locateCenterOnScreen(p+'confirmar.png', confidence=c)
        pyautogui.click(pos.x, pos.y)
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada')
        time.sleep(t)
    try:
        pos = pyautogui.locateCenterOnScreen(p+'jogar.png', confidence=c)
        pyautogui.click(pos.x, pos.y)
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada')
        time.sleep(t)
    try:
        pos = pyautogui.locateCenterOnScreen(p+'log.png', confidence=c)
        pyautogui.click(pos.x, pos.y)
        pyautogui.write('psdavid1911')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.write('Newpsd19')
        time.sleep(0.5)
        pyautogui.press('enter')
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada')
        time.sleep(t)
    try:
        pos = pyautogui.locateCenterOnScreen(p+'log2.png', confidence=c)
        pyautogui.click(pos.x, pos.y)
        pyautogui.write('psdavid1911')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.write('Newpsd19')
        time.sleep(0.5)
        pyautogui.press('enter')
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada')
        time.sleep(t)
    try:
        pos = pyautogui.locateCenterOnScreen(p+'encontrar.png', confidence=c)
        pyautogui.click(pos.x, pos.y)
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada')
        time.sleep(t)