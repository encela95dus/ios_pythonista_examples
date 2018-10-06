import scene, ui

class MyScene(scene.Scene):
    def setup(self):
        print(self.size, self.bounds, self.frame)
        self.label_node = scene.LabelNode('Hello World', 
            position=self.size/2.0, parent=self)
        self.sprite_node = scene.SpriteNode('Dog_Face', 
            position=(self.size[0]/2, self.size[1]/2-100), parent=self)
        self.shape_node = scene.ShapeNode(ui.Path.oval(0, 0, 50, 50), fill_color='red', 
            stroke_color='green', position=(self.size[0]/2, self.size[1]/2+100), parent=self)  
                                
scene.run(MyScene())
