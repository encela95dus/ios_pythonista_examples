import ui

class RadioButton(ui.View):
    def __init__(self, *args, **kwargs):
        super(RadioButton, self).__init__(*args, **kwargs)
        self.background_color = 'lightgray'
        if 'num_buttons' in kwargs:
            self.num_buttons = kwargs['num_buttons']
        else:
            self.num_buttons = 3
        if 'action' in kwargs:
            self.action = kwargs['action']
        else:
            self.action = None
        self.images = [ui.Image.named('iob:ios7_circle_filled_32'),
            ui.Image.named('iob:ios7_circle_outline_32')]
        x, y, w, h = self.frame
        w = w/self.num_buttons
        self.selected_index = 0
        for i in range(self.num_buttons):
            button = ui.Button(frame=(i*w, 0, w,h))
            button.image = self.images[1]
            button.action = self.button_action
            button.background_color = 'white'
            button.index = i
            self.add_subview(button)
        self.subviews[self.selected_index].image = self.images[0]
            
    def button_action(self, sender):
        self.subviews[self.selected_index].image = self.images[1]
        self.selected_index = sender.index
        sender.image = self.images[0]
        if self.action:
            self.action(self)
            
def button_action(sender):
    print(sender.selected_index)
           
v = ui.View(frame=(0,0,400, 400))
v.background_color = 'white'
r = RadioButton(frame=(100, 100, 200, 50), num_buttons=4, action=button_action)
r.border_width = 1
v.add_subview(r)
v.present('sheet')
            
            
            
