# import pynput #<-- Unused, check line 47.


import subprocess
import keyboard
from pynput.mouse import Button, Controller
import time
import random

# mouse = pynput.mouse.Controller() #<-- Unused, check line 47.

subprocess.Popen('MicrosoftEdge.exe')

for xy in range(10): #<-- Number of repeated searches.
    randomString = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    second_pass = False

    word_count = random.randint(2,4)

    for i in range(1, word_count):
        word_length = random.randint(3,7)
        if second_pass:
            randomString += " "
        for x in range(1, word_length):
            char_position = random.randint(0,24)
            randomChar = alphabet[char_position]
            if second_pass != True:
                randomString += randomChar.upper()
            else:
                randomString += randomChar
            second_pass = True

    randomString += "?"



    time.sleep(3)

    keyboard.write(randomString)
    keyboard.press_and_release('enter') #<-- Submit text.

    time.sleep(2)
    keyboard.press_and_release('alt+left') #<-- Back shortcut on keyboard.

    #mouse.press(Button.x1)
    #mouse.release(Button.x1) #<-- Back key on mouse, unused because of the need to point to the process window with mouse cursor. 

    time.sleep(1)

    keyboard.press_and_release('alt+d') #<-- Address bar toggle shortcut.
