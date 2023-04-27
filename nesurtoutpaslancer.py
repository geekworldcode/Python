from pynput.keyboard import Key, Controller

keyboard = Controller()

while 1:
    keyboard.press(Key.cmd)
    keyboard.press('d')
    keyboard.release('d')
