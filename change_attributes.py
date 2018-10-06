import scene, math


class ButtonNode(scene.SpriteNode):
    def __init__(self, title, *args, **kwargs):
        scene.SpriteNode.__init__(self, 'pzl:Button1', *args, **kwargs)
        self.title = title
        scene.LabelNode(title, color='blue', font=('Avenir Next', 20),
                        parent=self, position=(0, 0))
        
    def touch_began(self, touch):
        label_node = self.parent.label_node
        if self.title == 'change_font_name':
            font_name, font_size = label_node.font
            label_node.font  = ('Courier', font_size)
        elif self.title == 'change_font_size':
            font_name, font_size = label_node.font
            label_node.font  = (font_name, 40)
        elif self.title == 'change_color':
            label_node.color  = 'blue'
        elif self.title == 'rotate':
            label_node.rotation  = math.radians(30)


class MyScene(scene.Scene):
    def setup(self):
        center = self.size/2.0
        self.label_node = scene.LabelNode('Hello World', 
            position=center, parent=self)
        ButtonNode('change_font_name', parent=self, position=center - (300,  300))
        ButtonNode('change_font_size', parent=self, position=center - (100,  300))
        ButtonNode('change_color', parent=self, position=center + (100, -300))
        ButtonNode('rotate', parent=self, position=center + (300, -300))
           
    def touch_began(self, touch):
        for node in self.children:
            if touch.location in node.frame and hasattr(node, 'touch_began'):
                    node.touch_began(touch)
           

scene.run(MyScene())
