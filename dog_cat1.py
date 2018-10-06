import ui

dog = ui.Image('Dog_Face')
cat = ui.Image('Cat_Face')



def set_dog(sender):
    v['imageview1'].image = dog
    
def set_cat(sender):
    v['imageview1'].image = cat

v = ui.View(frame=(0,0,500,500))
v.add_subview(ui.ImageView(frame=(100, 50,200,200),
                name='imageview1', text='0', alignment=ui.ALIGN_CENTER, border_width=1))
v['imageview1'].image = dog
v.add_subview(ui.Button(frame=(50,300,100,100),
                name='button1', title='dog', action=set_dog, corner_radius=50))
v['button1'].width = 100
v['button1'].height = 100
v.add_subview(ui.Button(frame=(250,300,100,100),
                name='button2',title='cat', action=set_cat, corner_radius=50))
v['button2'].width = 100
v['button2'].height = 100
v['button1'].background_image = dog
v['button1'].background_color = 'lightgray'
v['button2'].background_image = cat
v['button2'].background_color = 'lightgray'
v.present('sheet')
