import ui

def inc1(sender):
    t = int(sender.superview['label1'].text)
    sender.superview['label1'].text = str(t+1)
       
def dec1(sender):
    t = int(sender.superview['label1'].text)
    sender.superview['label1'].text = str(t-1)
    
v = ui.load_view()
v.present('sheet')
