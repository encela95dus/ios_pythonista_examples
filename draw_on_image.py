'''
A simple 'app' to draw on image based on sketch example
'''

import ui
import photos
import console

canvas_size = 500
image_background = ui.Image('test:Mandrill')

class PathView (ui.View):
    def __init__(self, frame):
        self.frame = frame
        self.flex = 'WH'
        self.path = None
        self.action = None

    def touch_began(self, touch):
        x, y = touch.location
        self.path = ui.Path()
        self.path.line_width = 8.0
        self.path.line_join_style = ui.LINE_JOIN_ROUND
        self.path.line_cap_style = ui.LINE_CAP_ROUND
        self.path.move_to(x, y)

    def touch_moved(self, touch):
        x, y = touch.location
        self.path.line_to(x, y)
        self.set_needs_display()

    def touch_ended(self, touch):
        # Send the current path to the SketchView:
        if callable(self.action):
            self.action(self)
        # Clear the view (the path has now been rendered
        # into the SketchView's image view):
        self.path = None
        self.set_needs_display()

    def draw(self):
        if self.path:
            self.path.stroke()


class SketchView (ui.View):
    def make_buttonitem(self, title, action):
        buttonitem = ui.ButtonItem()
        buttonitem.title = title
        buttonitem.action = action
        return buttonitem
        
    def __init__(self, width=500, height=500):
        self.bg_color = 'white'
        iv = ui.ImageView(frame=(0, 0, width, height))
        iv.image = self.bg_image = image_background
        pv = PathView(frame=self.bounds)
        pv.action = self.path_action
        self.add_subview(iv)
        self.add_subview(pv)
        save_button = self.make_buttonitem('save', self.save_action)
        show_button = self.make_buttonitem('show', self.show_action)
        copy_button = self.make_buttonitem('clear', self.clear_action)
        self.right_button_items = [save_button, show_button, copy_button]  
        self.image_view = iv

    def path_action(self, sender):
        path = sender.path
        old_img = self.image_view.image
        width, height = canvas_size, canvas_size
        with ui.ImageContext(width, height) as ctx:
            if old_img:
                old_img.draw(0,0,self.width, self.height)
            path.stroke()
            self.image_view.image = ctx.get_image()

    def clear_action(self, sender):
        self.image_view.image = self.bg_image
        
    def show_action(self, sender):
        if self.image_view.image:
            with ui.ImageContext(self.width, self.height) as ctx:
                self.image_view.image.draw()
                img = ctx.get_image()
                img.show()
                console.hud_alert('Showed')
        else:
            console.hud_alert('No Image', 'error')

    def save_action(self, sender):
        if self.image_view.image:
            with ui.ImageContext(self.width, self.height) as ctx:
                self.image_view.image.draw()
                img = ctx.get_image()
                photos.save_image(img)
                console.hud_alert('Saved')
        else:
            console.hud_alert('No Image', 'error')

sv = SketchView(canvas_size, canvas_size)
sv.name = 'Sketch'
sv.frame=(0,0,canvas_size, canvas_size)
sv.present('sheet') 
