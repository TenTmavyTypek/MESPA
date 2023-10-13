import subprocess
import keyboard
import random
import time
import pyautogui

# Open Microsoft Edge
subprocess.Popen('MicrosoftEdge.exe')

# Number of repeated searches
search_count = 10

for _ in range(search_count):
    random_query = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    second_pass = False

    # Generate a random word count
    word_count = random.randint(2, 4)

    for _ in range(word_count):
        word_length = random.randint(3, 7)

        # Add space if it's not the first word
        if second_pass:
            random_query += " "

        for _ in range(word_length):
            char_position = random.randint(0, 25)
            random_char = alphabet[char_position]

            # Make the first character uppercase
            if not second_pass:
                random_query += random_char.upper()
            else:
                random_query += random_char

            second_pass = True

    random_query += "?"

    # Wait before typing and sending the query
    time.sleep(3)
    keyboard.write(random_query)
    keyboard.press_and_release('enter')  # Submit text

    # Wait for the search results to load
    time.sleep(2)

    # Navigate back using the keyboard shortcut
    keyboard.press_and_release('alt+left')

    # Wait for a moment before refocusing on the address bar
    time.sleep(1)
    keyboard.press_and_release('alt+d')  # Address bar toggle shortcut

# Display a message to the user
keyboard.write("The searches are complete. You can now close the Microsoft Edge browser.")

# Close Microsoft Edge using pyautogui
pyautogui.hotkey('alt', 'f4')