import ui
import clipboard

def inc1(sender):
    t = int(sender.superview['label1'].text)
    sender.superview['label1'].text = str(t+1)
       
def dec1(sender):
    t = int(sender.superview['label1'].text)
    sender.superview['label1'].text = str(t-1)

def save_action(sender):    
    clipboard.set(v['label1'].text)
   
def clear_action(sender):   
    v['label1'].text = '0'
    
v = ui.load_view()

save_button = ui.ButtonItem()
save_button.title = 'Save'
save_button.action = save_action
clear_button = ui.ButtonItem()
clear_button.title = 'Clear'
clear_button.tint_color = 'red'
clear_button.action = clear_action
v.right_button_items = [save_button, clear_button]

v.present('sheet')
