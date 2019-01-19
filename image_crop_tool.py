import ui, console, clipboard
import os
import math
from PIL import Image
import io

def ui2pil(ui_img):
    return Image.open(io.BytesIO(ui_img.to_png()))

def pil2ui(pil_img):
    with io.BytesIO() as buffer:
        pil_img.save(buffer, format='PNG')
        return ui.Image.from_data(buffer.getvalue())
    
class ShapeView(ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_location = None 
        x1,y1,self.w1,self.h1 = self.frame #(150, 150,100,100)
        
                
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

def create_image():
    img = None
    x1,y1,w1,h1 = main_view['view1'].frame
    x2,y2,w2,h2 = main_view['imageview1'].frame    
    x,y = x1 -x2, y1-y2
    im1 = main_view['imageview1'].image
    pim0 = ui2pil(im1)
    pim1 = pim0.resize((int(w2),int(h2)))
    pim2 = pim1.copy().crop((int(x),int(y),int(x+w1),int(y+h1)))
    im2 = pil2ui(pim2)
    with ui.ImageContext(w1,h1) as ctx:  
        im2.draw()
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
main_view['imageview1'].image = ui.Image('test:Mandrill')
save_button = make_buttonitem('save', save_action)
show_button = make_buttonitem('show', show_action)
copy_button = make_buttonitem('copy', copy_action)
main_view.right_button_items = [save_button, show_button, copy_button]
main_view.present('sheet')
