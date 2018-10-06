import scene


class ButtonNode(scene.SpriteNode):
    def __init__(self, title, *args, **kwargs):
        scene.SpriteNode.__init__(self, 'pzl:Button1', *args, **kwargs)
        self.title = title
        scene.LabelNode(title, color='blue', font=('Avenir Next', 20),
                        parent=self, position=(0, 0))
        
    def touch_began(self, touch):
        sprite = self.parent.sprite
        x, y = sprite.position
        if self.title == '←':
            sprite.position = max(x - 20, 0), y
        elif self.title == '→':
            sprite.position = min(x + 20, self.parent.size.w), y
        elif self.title == '↓':
            sprite.position = x, max(y - 20, 0)
        elif self.title == '↑':
            sprite.position = x, min(y + 20, self.parent.size.h)


class MyScene(scene.Scene):
    def setup(self):
        center = self.size/2
        self.sprite = scene.SpriteNode('Dog_Face', parent=self, position=center)
        ButtonNode('←', parent=self, position=center - (300,  300))
        ButtonNode('→', parent=self, position=center - (100,  300))
        ButtonNode('↓', parent=self, position=center + (100, -300))
        ButtonNode('↑', parent=self, position=center + (300, -300))
           
    def touch_began(self, touch):
        for node in self.children:
            if touch.location in node.frame and hasattr(node, 'touch_began'):
                    node.touch_began(touch)
           

scene.run(MyScene())
