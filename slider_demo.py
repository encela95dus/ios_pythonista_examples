import ui

currentval = .5


class CustomView(ui.View):                   
    def draw(self):
        global currentval
        
        x,y,w,h = self.frame
        path = ui.Path.rect(0,0, currentval*w, h)
        ui.set_color((1.0, 0.4, 0.4, 1.0))
        path.fill()

def slider_action1(sender):
    sender.superview['label1'].text = str(sender.value)
        
def slider_action2(sender):
    global currentval
    
    currentval = sender.value
    sender.superview['view1'].set_needs_display()


v = ui.load_view()
v.present('sheet')
