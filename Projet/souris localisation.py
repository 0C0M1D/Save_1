#Controle de la souris
from pynput.mouse import Controller, Button

mouse=Controller()
while True:
    print(mouse.position)