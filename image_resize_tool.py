import ui
import math, clipboard

class ImageSizeView(ui.View):                                   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_location = None
                                  
    def touch_began(self, touch):
        self.current_location = touch.location
        
    def change_size(self):
        sv = self.superview
        sv['textfield1'].text = str(self.width)
        sv['textfield2'].text = str(self.height)
        self.remove_subview(self.iv) 
        self.iv = ui.ImageView(frame=(0,0,self.width, self.height), image=self.image)
        self.add_subview(self.iv)   
        
    def touch_moved(self, touch):
        sgindex = self.superview['segmentedcontrol1'].selected_index
        x,y = touch.location
        if self.current_location:
            x1, y1 = self.current_location 
        else:
            self.current_location = x,y
            return 
        self.current_location = x,y                              
        if sgindex == 0:
            self.width += (x-x1)
            self.height += (y-y1) 
            self.change_size()            
        elif sgindex == 1:
            self.width += (x-x1)
            self.change_size()         
        elif sgindex == 2:
            self.height += (y-y1) 
            self.change_size()          
                                                  
    def touch_ended(self, touch):
        self.current_location = None
        
def create_image():
    img = None
    x,y,w,h = v['view1'].frame
    with ui.ImageContext(w,h) as ctx:  
        v['view1'].subviews[0].image.draw(0,0,w,h)
        img = ctx.get_image()
    return img
        
def save_action(sender):
    img = create_image()
    with open('image_file.png', 'wb') as fp:
        fp.write(img.to_png())
    console.hud_alert('image saved in the file image_file.png')

def copy_action(sender):
    img = create_image()        
    clipboard.set_image(img)    
    
def show_action(sender):
    img = create_image()
    img.show() 
    
def make_buttonitem(title, action):
    buttonitem = ui.ButtonItem()
    buttonitem.title = title
    buttonitem.action = action
    return buttonitem

v = ui.load_view()
x,y,w,h = v['view1'].frame
v['view1'].image = ui.Image('test:Mandrill')
v['view1'].iv = ui.ImageView(frame=(0, 0, w, h), name='imageview1', image=v['view1'].image)
v['view1'].add_subview(v['view1'].iv) 
save_button = make_buttonitem('save', save_action)
show_button = make_buttonitem('show', show_action)
copy_button = make_buttonitem('copy', copy_action)
v.right_button_items = [save_button, show_button, copy_button]  
v.present('sheet')
