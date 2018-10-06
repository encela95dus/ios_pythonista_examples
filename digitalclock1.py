import ui
from time import localtime

class DigitalClock(ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_interval = .1
        
    def draw(self):
        t = localtime()
        ui.draw_string("{:02}:{:02}:{:02}".format(
            t.tm_hour, t.tm_min, t.tm_sec),
            font=('Helvetica', 20),
            rect=(100, 100,0,0),
            alignment=ui.ALIGN_CENTER)
            
    def update(self):
        self.set_needs_display()
    
v = DigitalClock(frame=(0,0,300, 300))
v.present('sheet')
