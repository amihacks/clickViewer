from django.core.signals import request_finished, request_started
from django.dispatch import receiver
from pynput.mouse import Listener

def on_click(x, y, button, pressed):    
    if pressed and button == button.left:
        print ('Left clicked at ({0}, {1})'.format(x, y))

@receiver(request_finished)
def listener_join(sender, **kwargs):
    with Listener(on_click=on_click) as listnr:
        listnr.join()

@receiver(request_started)
def listener_stop(sender, **kwargs):
    with Listener(on_click=on_click) as listnr:
        listnr.stop()