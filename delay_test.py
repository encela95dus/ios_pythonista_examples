import ui
from functools import partial

def delay_action(sender):
    sender.title = 'bye'

def button_tapped(sender):
    sender.title = 'Hello'
    ui.delay(partial(delay_action, sender), 3)

view = ui.View(frame=(0,0,400, 400), name='Delay Test')     
view.background_color = 'white'                       
button = ui.Button(title='Tap me!', border_width=1)                   
button.center = (view.width * 0.5, view.height * 0.5) 
button.action = button_tapped                         
view.add_subview(button)                              
view.present('sheet')                                 
