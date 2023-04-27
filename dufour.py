from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller, Button
import webbrowser
import time

keyboard = Controller()
mouse = Controller()

mode = input("Quel mode choisis tu (1-2)?:")
if (mode == '2'):
    while True:
        print(mouse.position)


temps = int(input("Temps entre les pages ?:"))


while True:
    webbrowser.open('https://www.google.fr/', new=2)

    time.sleep(int(temps))

    for i in "le mot":
        keyboard.press(i)
        keyboard.release(i)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)