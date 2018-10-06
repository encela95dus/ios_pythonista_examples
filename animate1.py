import ui

def animate_color(v, col):
    def a():
        v.background_color = col
    ui.animate(a, 2.0)

def blue_action(sender):
    v = sender.superview
    animate_color(v['view1'], 'blue')
  
def red_action(sender):
    v = sender.superview
    animate_color(v['view1'], 'red')    

v = ui.load_view()
v.present('sheet')
