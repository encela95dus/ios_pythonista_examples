import ui, photos

def animate_movex(v, x):
    def a():
        v.x = x
    ui.animate(a, 2.0)

def animate_alpha(v, alpha):
    def a():
        v.alpha = alpha
    ui.animate(a, 2.0)
    
def animate_scale(v, w, h):
    def a():
        v.width = w
        v.height = h
    ui.animate(a, 2.0)

def scale_orig(sender):
    v = sender.superview
    animate_scale(v['view1'], weight, height)
  
def scale_0(sender):
    v = sender.superview
    animate_scale(v['view1'], 0, 0)
    
def alpha_orig(sender):
    v = sender.superview
    animate_alpha(v['view1'], 1)
  
def alpha_0(sender):
    v = sender.superview
    animate_alpha(v['view1'], 0)
    
def movex_orig(sender):
    v = sender.superview
    animate_movex(v['view1'], x1)
  
def movex_0(sender):
    v = sender.superview
    animate_movex(v['view1'], 0)    

v = ui.load_view()
stored_image = ui.Image('test:Mandrill')
x1,y1,weight,height = v['view1'].frame
img_view = ui.ImageView(frame=(0,0,weight, height), name='imageview1', image=stored_image)
v['view1'].add_subview(img_view)
v.present('sheet')
