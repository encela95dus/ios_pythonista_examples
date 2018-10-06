import ui, console
import os
import math

def save_action(sender):
    with open('image_file.png', 'wb') as fp:
        fp.write(img.to_png())
    console.hud_alert('image saved in the file image_file.png')
    
def showimage_action(sender):
    img.show() 

def create_image():
    img = None
    with ui.ImageContext(500, 500) as ctx:    
        path = ui.Path.oval(50,50,400, 100)
        ui.set_color((1.0, 0.4, 0.4, 1.0))
        path.fill()
        path.line_width = 10.0
        ui.set_color((0.8, 1.0, 0.5, 1.0))
        path.stroke()
        ui.draw_string('Label', rect=(50,175,400,100),
                 font=tuple(('Georgia', 20)),
                 color=(0.4, 0.6, 1.0, 1.0), alignment=0,
                 line_break_mode=4)
        ui.Image("Dog_Face").draw(50,200,300,300)       
        img = ctx.get_image()
    return img

img = create_image()
#img.show()
main_view = ui.View(frame=(0,0,500,500))
imgview = ui.ImageView(frame=(0,0,500,500))
imgview.image = img
main_view.add_subview(imgview)
save_button = ui.ButtonItem()
save_button.title = 'Save'
save_button.action = save_action
show_button = ui.ButtonItem()
show_button.title = 'Show'
show_button.action = showimage_action
main_view.right_button_items = [save_button, show_button]
main_view.present('sheet')
