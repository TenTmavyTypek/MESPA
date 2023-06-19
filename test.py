from pynput.mouse import Listener
def on_click(x, y, button, pressed):
    if pressed:
       print(button)
   
# Collect events until released
with Listener(on_click=on_click) as listener:
    listener.join()