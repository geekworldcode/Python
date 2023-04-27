import webbrowser
import time
from pynput.mouse import Controller, Button

mouse = Controller()

#while True:
    #print(mouse.position)

lien = input("Lien de la vidéo (Youtube):")

mouse.position = (2389, 1059)

mouse.press(Button.left)
mouse.release(Button.left)

mouse.position = (2493, 1013)

time.sleep(0.1)
mouse.press(Button.left)
mouse.release(Button.left)

mouse.position = (0, 0)

mouse.press(Button.left)
mouse.release((Button.left))

while True:
    webbrowser.open(lien, new=2)
    time.sleep(1.5)

