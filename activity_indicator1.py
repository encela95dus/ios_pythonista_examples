import ui, time
from functools import partial

def delay_action(sender):
    v1 = sender.superview['view1']
    v1.remove_subview(v1['activity'])
    v1.add_subview(img)
    
def reset_action(sender):
    v1 = sender.superview['view1']
    v1.remove_subview(v1['imageview1'])

def start_action(sender):
    v1 = sender.superview['view1']
    a=ui.ActivityIndicator(name='activity')
    a.center=v1.bounds.center()
    a.start_animating()
    v1.add_subview(a)
    ui.delay(partial(delay_action, sender), 3)


v = ui.load_view()
x,y,w,x = v['view1'].frame
img = ui.ImageView(frame=(0,0,w,x), name='imageview1', image=ui.Image('Dog_Face'))
v['view1'].add_subview(img)
v.present('sheet')

