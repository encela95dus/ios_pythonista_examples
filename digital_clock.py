import scene
from time import localtime

class MyScene(scene.Scene):
    def setup(self):
        self.digital_clock = scene.LabelNode("", 
                                position=self.size/2, 
                                parent=self)
    def update(self):
        t = localtime()
        self.digital_clock.text = "{:02}:{:02}:{:02}".format(
                                 t.tm_hour, t.tm_min, t.tm_sec)

scene.run(MyScene())
