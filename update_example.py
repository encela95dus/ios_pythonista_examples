import scene

class MyScene(scene.Scene):
    def setup(self):
        self.cnt = 0        
        self.test_label = scene.LabelNode('Hello World', 
            position=self.size/2.0, parent=self)
            
    def update(self):
        self.cnt = (self.cnt+1)%100000
        self.test_label.text = 'HelloWorld ' + str(self.cnt)
           
scene.run(MyScene())
