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
        with ui.GState():
            ui.concat_ctm(ui.Transform.rotation(0.78))
            ui.draw_string('    Rotated text', rect=(200, 100, 200,200), 
                                        font=('<system>', 20), color='blue')
        ui.draw_string('Not rotated', rect=(50, 100, 200,200), 
                        font=('<system>', 20), color='red')    
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

