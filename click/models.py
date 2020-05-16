from django.db import models
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed and button == button.left:
        print ('Left clicked at ({0}, {1})'.format(x, y))

with Listener(on_click=on_click) as listnr:
    listnr.join()
