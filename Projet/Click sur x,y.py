#Controle de la souris
from pynput.mouse import Controller, Button

mouse=Controller()

mouse.position=(x,y)

mouse.press(Button.left)
mouse.release(Button.left)


