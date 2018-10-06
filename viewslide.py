import ui

def hide_action(sender):
    s = sender.superview
    s['view1'].hidden = True
    s2 = s['view2']
    def a():
        s2.transform=ui.Transform.scale(1.0, 1.33).concat(ui.Transform.translation(0,-100))
        
    ui.animate(a, 1.0)

def reveal_action(sender):
    s = sender.superview
    s2 = s['view2']
    def a():
        s2.transform=ui.Transform.scale(1.0, 1.0).concat(ui.Transform.translation(0,0))
        s['view1'].hidden = False
        
    ui.animate(a, 1.0)

v = ui.load_view()
v.present('sheet')
