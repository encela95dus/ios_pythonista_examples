import scene  

class MyScene(scene.Scene):
    def setup(self):
        self.label_node = scene.LabelNode('A',
                    position=(100,400), parent=self)
        self.animate_action = scene.Action.move_to(340, 400, 2)
            
    def touch_ended(self, touch):
        self.label_node.run_action(self.animate_action)

scene.run(MyScene())
