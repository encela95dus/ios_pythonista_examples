import scene, ui
from time import localtime

class MyScene(scene.Scene):
    def setup(self):
        self.stop_watch = scene.LabelNode("", position=self.size/2, parent=self)
        self.state = 'run'
        self.value = 0

    def update(self):
        if self.state == 'run':
            self.value += 1
            v = (self.value//(3600*60), self.value//3600, self.value//60)
            t = (v[0], v[1]%60, v[2]%60)
            self.stop_watch.text = "{:02}:{:02}:{:02}".format(*t)
        
    def touch_began(self, touch):
        if self.state == 'run':
            self.state = 'stop'
        elif self.state == 'stop':
            self.state = 'run'
            self.value = 0

scene.run(MyScene())
