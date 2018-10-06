import scene
import math
from functools import partial
import random
 
class TextAnimate(scene.Scene):
    def setup(self):
        #self.label_text = 'ABCDEFGHIJKLMNOPQR'
        self.label_text = 'abcdefghijklmnopqrstuvwxyz'
        length = len(self.label_text)
        center = self.bounds.center()
        self.font_size = 60
        self.pixel_size = .6*self.font_size
        self.main_node = scene.Node(position=(center[0]-length/2.0*self.pixel_size,
            center[1]), parent=self)
        self.label_node = [None]*len(self.label_text)
        self.pos1 = [None]*len(self.label_text)
        self.pos2 = [None]*len(self.label_text)
        for i in range(len(self.label_text)):
            self.pos1[i] = (800*random.random()+100, 600*random.random()-300)
            self.pos2[i] = (self.pixel_size*i*1.0, 0.0)
        A = scene.Action
        for i in range(len(self.label_text)):
            self.label_node[i] = scene.LabelNode(self.label_text[i],
                    font=('Courier', self.font_size),
                    position=self.pos1[i], parent=self.main_node)
            animate_action = A.repeat(A.sequence(
                                        A.move_to(self.pos2[i][0], self.pos2[i][1], 8),
                                        A.move_to(self.pos1[i][0], self.pos1[i][1], 8)), 0)
            self.label_node[i].run_action(animate_action)

scene.run(TextAnimate())
