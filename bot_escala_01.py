import pyautogui,time,pygetwindow,os

# inicia o edge
os.startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

# configura o edge
janela = pygetwindow.getWindowsWithTitle('Nova guia')[0]
janela.activate()
janela.maximize()
time.sleep(2)

# inicia o calendar
pyautogui.hotkey('alt','d')
pyautogui.write(r'http://calendar.google.com')
pyautogui.press('enter')








