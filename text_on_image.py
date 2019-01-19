import ui, console, clipboard
import os
import math

input_info = ('text', 'Dog')
#input_info = ('image', 'Snake')
#input_info = ('shape',  'oval' )
  
class ShapeView(ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_location = None 
        x1,y1,self.w1,self.h1 = self.frame 
               
    def touch_began(self, touch):
        self.current_location = touch.location
        
    def touch_moved(self, touch):
        x,y = touch.location
        self.x2,self.y2,self.w2,self.h2 = self.superview['imageview1'].frame
        if self.current_location:
            x1, y1 = self.current_location 
        else:
            self.current_location = x,y
            return                               
        if max(abs(x-x1), abs(y-y1)) > 3:
            self.current_location = x,y
            self.x += (x-x1)
            self.y += (y-y1)
        self.x = min(self.x2+self.w2-self.w1, max(self.x2, self.x))
        self.y = min(self.y2+self.h2-self.h1, max(self.y2, self.y))
        
    def touch_ended(self, touch):
        self.current_location = None
        
def make_shape(shape_type, x, y, w, h, stroke_color=None, fill_color=None,
            stroke_width=0, corner_radius=0):
    if shape_type == "oval":
        path = ui.Path.oval(x,y,w,h)
    elif shape_type == "rectangle":
        path = ui.Path.rect(x,y,w,h)
    elif shape_type == "rounded_rectangle":
        path = ui.Path.rounded_rect(x,y,w,h)
    if fill_color:
        ui.set_color(fill_color)
        path.fill()
    else:
        ui.set_color((.8,.8,.8,1.0))
        path.fill()
    if stroke_color:
        ui.set_color(stroke_color)
        path.line_width = stroke_width
        path.stroke()
        
def create_image():
    img = None
    x1,y1,w1,h1 = main_view['view1'].frame
    x2,y2,w2,h2 = main_view['imageview1'].frame    
    x,y = x1 -x2, y1-y2
    im1 = main_view['imageview1'].image
    with ui.ImageContext(w2,h2) as ctx:  
        im1.draw(0, 0, w2, h2)
        if input_info[0] == 'text':
            ui.draw_string(input_info[1], rect=(x, y, 0, 0))
        elif input_info[0] == 'image':
            ui.Image(input_info[1]).draw(x,y, w1, h1)
        elif input_info[0] == 'shape':
            make_shape(input_info[1], x,y,w1,h1)
        img = ctx.get_image()
    return img
    
def save_action(sender):
    img = create_image()
    with open('image_file.png', 'wb') as fp:
        fp.write(img.to_png())
    console.hud_alert('image saved in the file image_file.png')
    
def show_action(sender):
    img = create_image()
    img.show()
    
def copy_action(sender):
    img = create_image()        
    clipboard.set_image(img)    
       
def make_buttonitem(title, action):
    buttonitem = ui.ButtonItem()
    buttonitem.title = title
    buttonitem.action = action
    return buttonitem

main_view = ui.load_view()
main_view['imageview1'].image = ui.Image('Dog_Face') 
save_button = make_buttonitem('save', save_action)
show_button = make_buttonitem('show', show_action)
copy_button = make_buttonitem('copy', copy_action)
main_view.right_button_items = [save_button, show_button, copy_button]
main_view.present('sheet')
