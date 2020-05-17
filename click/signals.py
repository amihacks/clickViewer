from django.core.signals import request_finished, request_started
from django.dispatch import receiver
from pynput.mouse import Listener

def on_click(x, y, button, pressed):    
    if pressed and button == button.left:
        print ('Left clicked at ({0}, {1})'.format(x, y))
       

listeners = []

def listener_join(sender, **kwargs):
    listeners = [Listener(on_click=on_click)]
    listeners[0].start()


def listener_stop(sender, **kwargs):
    if len(listeners) > 0:
        listeners[0].stop()
        

request_started.connect(listener_stop, dispatch_uid='stop')
request_finished.connect(listener_join, dispatch_uid='start')

