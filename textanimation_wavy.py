import scene
import math
from functools import partial

def custom_action(idx, node, progress):
    gp = node.parent.parent
    txt = gp.label_text
    phase = 2*math.pi*idx/len(txt)
    x,y = node.position
    node.position = x, 50*math.sin(2*math.pi*progress+phase)
     
import math

class TextAnimate(scene.Scene):
    def setup(self):
        #self.label_text = 'ABCDEFGHIJKLMNOPQR'
        self.label_text = 'abcdefghijklmnopqrstuvwxyz'
        length = len(self.label_text)
        center = self.bounds.center()
        self.font_size = 40
        self.pixel_size = .6*self.font_size
        self.main_node = scene.Node(position=(center[0]-length/2.0*self.pixel_size,
            center[1]), parent=self)
        self.label_node = [None]*len(self.label_text)
        A = scene.Action
        for i in range(len(self.label_text)):
            self.label_node[i] = scene.LabelNode(self.label_text[i],
                    font=('Courier', self.font_size),
                    position=(self.pixel_size*i, 0), parent=self.main_node)
            custom_action_i = partial(custom_action, i)
            animate_action = A.repeat(A.call(custom_action_i, 5), 0)
            self.label_node[i].run_action(animate_action)

scene.run(TextAnimate())
