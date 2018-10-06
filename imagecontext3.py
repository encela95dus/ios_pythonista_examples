import ui, console
import os
import math

def save_action(sender):
    with open('image_file.png', 'wb') as fp:
        fp.write(img.to_png())
    console.hud_alert('image saved in the file image_file.png')
    
def showimage_action(sender):
    img.show() 
    
def make_polygon(num_sides, x=0, y=0, radius=100, phase=0, line_width=5): 
    path = ui.Path()
    path.move_to(x,y)
    path.line_width = line_width
    for i in range(num_sides):
        t = 2*math.pi*i/num_sides
        x1, y1 = radius+radius*math.cos(t+phase), radius+radius*math.sin(t+phase)
        if i:
            path.line_to(x+x1, y+y1)
        else:
            path.move_to(x+x1,y+y1)
    path.close() 
    return path    

def create_image():
    img = None
    with ui.ImageContext(500, 500) as ctx:  
        path = make_polygon(5, 100, 100, 150)  
        ui.set_color((1.0, 0.4, 0.4, 1.0))
        path.fill()
        path.line_width = 10.0
        ui.set_color((0.8, 1.0, 0.5, 1.0))
        path.stroke()
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
