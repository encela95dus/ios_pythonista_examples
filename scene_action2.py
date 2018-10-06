import scene  

class MyScene(scene.Scene):
    def setup(self):
        self.label_node = scene.LabelNode('A',
                    position=(100,400), parent=self)
        self.start_flag = False
        
    def update(self):
        if self.start_flag:
            x,y = self.label_node.position
            if x < 340:
                self.label_node.position = (x+2, y)
            else:
                self.start_flag = False
            
    def touch_ended(self, touch):
        self.start_flag = True

scene.run(MyScene())
