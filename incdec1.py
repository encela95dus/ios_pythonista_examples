import ui

def inc1(sender):
    t = int(sender.superview['label1'].text)
    sender.superview['label1'].text = str(t+1)
       
def dec1(sender):
    t = int(sender.superview['label1'].text)
    sender.superview['label1'].text = str(t-1)
    
v = ui.View(frame=(0,0,400,400))
v.add_subview(ui.Label(frame=(100, 50,200,50),
                name='label1', text='0', alignment=ui.ALIGN_CENTER,border_width=1))
v.add_subview(ui.Button(frame=(50,200,100,50),
                name='button1', title='inc', action=inc1, border_width=1))
v['button1'].width = 100
v['button1'].height = 50
v['button1'].image = ui.Image('iob:ios7_plus_empty_24')
v.add_subview(ui.Button(frame=(250,200,100,50),
                name='button2',title='dec', action=dec1, border_width=1))
v['button2'].width = 100
v['button2'].height = 50
v['button2'].image = ui.Image('iob:ios7_minus_empty_24')
v.present('sheet')
