import scene

def custom_action(node, progress):
    ntime = node.parent.duration
    i = ntime - int(ntime*progress)
    if i >= 0:
        node.text = str(i)

class MyScene(scene.Scene):
    def setup(self):
        self.test_label = scene.LabelNode('0', 
            position=self.size/2.0, parent=self)
        self.duration = 10
        self.activate_timer_label = scene.LabelNode('Activate Timer',
            position=(self.size[0]/2-200, self.size[1]/2-100),
            parent=self)
        self.stop_timer_label = scene.LabelNode('Stop Timer',
            position=(self.size[0]/2, self.size[1]/2-100),
            parent=self)
        self.reset_timer_label = scene.LabelNode('Reset Timer',
            position=(self.size[0]/2+200, self.size[1]/2-100),
            parent=self)
            
    def touch_began(self, touch):
        if touch.location in self.stop_timer_label.frame:
            self.test_label.remove_action('timer_action')
            return
        if touch.location in self.reset_timer_label.frame:
            self.test_label.remove_action('timer_action')
            self.test_label.text = '0'
            return
        if touch.location in self.activate_timer_label.frame:
            timer_action = scene.Action.call(custom_action, self.duration)
            self.test_label.run_action(timer_action, 'timer_action')
           
scene.run(MyScene())



