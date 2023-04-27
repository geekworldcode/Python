from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller, Button
import webbrowser
import time

keyboard = Controller()
mouse = Controller()

webbrowser.open('https://www.google.fr/', new=2)

