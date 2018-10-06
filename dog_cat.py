import ui

dog = ui.Image('Dog_Face')
cat = ui.Image('Cat_Face')



def set_dog(sender):
    v['imageview1'].image = dog
    
def set_cat(sender):
    v['imageview1'].image = cat

v = ui.load_view()
v.background_color = 'gray'
v['imageview1'].image = dog
v['button1'].background_image = dog
v['button1'].background_color = 'lightgray'
v['button2'].background_image = cat
v['button2'].background_color = 'lightgray'
v.present('fullscreen')
