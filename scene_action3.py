import scene  

def custom_action(node, progress):
    x,y = node.initial_position
    node.position = (x+240*progress, y)

class MyScene(scene.Scene):
    def setup(self):
        self.label_node = scene.LabelNode('A',
                    position=(100,400), parent=self)
        x,y = self.label_node.position
        self.label_node.initial_position = (x,y)
        self.animate_action = scene.Action.call(custom_action, 2)
            
    def touch_ended(self, touch):
        self.label_node.run_action(self.animate_action)

scene.run(MyScene())
