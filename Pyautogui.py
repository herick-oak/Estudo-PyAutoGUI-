#first bot
import pyautogui
import time

pyautogui.PAUSE = 0.3 # ele pausa um tempo nas automacoes

#---------------- Pegar posição mouse e tela
time.sleep(5)
print(pyautogui.position())
# print(pyautogui.size())

# --------------- Mouse fuctions
time.sleep(5)
#pyautogui.click(x=499, y=11) # (x=499, y=11),i can choice the button
# pyautogui.moveTo(x=499, y=11,duration=1)
# pyautogui.scroll()

#---------------- Funcoes teclado

# pyautogui.write("Se inscreve")
# pyautogui.hotkey("CTRL","c") #cONSIGO FAZER COMANDOS
# pyautogui.press("win") #preciona a tela, print(pyautogui.KEYBOARD_KEYS) VAI DAR TODOS OS COMANDOS

# pyautogui.press("win")
# pyautogui.write("Opera")
# pyautogui.press("enter")