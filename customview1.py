import ui
import os
import math

class CustomView(ui.View):
    def __init__(self, *args, **kwargs):
        frame = (0,0, 500, 500)
        super().__init__(frame=frame, *args, **kwargs)
        
    def draw(self):
        path = ui.Path.oval(50,50,400, 100)
        ui.set_color((1.0, 0.4, 0.4, 1.0))
        path.fill()
        path.line_width = 10.0
        ui.set_color((0.8, 1.0, 0.5, 1.0))
        path.stroke()
        ui.draw_string('Label', rect=(50,175,400,100),
                 font=tuple(('Georgia', 20)),
                 color=(0.4, 0.6, 1.0, 1.0), alignment=0,
                 line_break_mode=4)
        ui.Image("Dog_Face").draw(50,200,300,300)

main_view = CustomView() 
main_view.present('sheet')
