import ui, math


class ImageMaskPolygon(ui.View):
    def make_polygon(self, num_sides, x=0, y=0, radius=100, phase=0, line_width=5): 
        path = ui.Path()
        path.move_to(x,y)
        path.line_width = line_width
        for i in range(num_sides):
            t = 2*math.pi*i/num_sides
            x1, y1 = radius+radius*math.cos(t+phase), radius+radius*math.sin(t+phase)
            if i:
                path.line_to(x+x1, y+y1)
            else:
                path.move_to(x+x1,y+y1)
        path.close() 
        return path  
        
    def draw(self):
        x,y,w,h = self.bounds
        poly = self.make_polygon(6, x=x, y=y, radius=w/2)
        rect = ui.Path.rect(*self.bounds)
        poly.append_path(rect)
        poly.eo_fill_rule = True
        poly.add_clip()
        ui.set_color('lightgreen')
        rect.fill()
    
class TestClass(ui.View):
    def __init__(self, image_mask = None, *args, **kwargs):
        ui.View.__init__(self, *args, **kwargs)      
        self.iv = ui.ImageView()
        self.iv.image = ui.Image('test:Mandrill')
        self.iv.frame = self.bounds
        self.add_subview(self.iv)
        self.add_subview(image_mask)
        
        
if __name__ == '__main__':
    f = (0,0, 400, 400)
    im = ImageMaskPolygon(frame=f)
    tc = TestClass(im, frame = f)
    tc.present('sheet')
