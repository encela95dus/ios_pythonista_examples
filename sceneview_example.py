import ui, scene

img_label = 'dog'

def set_dog(sender):
    global img_label
    img_label = 'dog'
    
def set_cat(sender):
    global img_label
    img_label = 'cat'    

class MyScene(scene.Scene):
    def setup(self):
        print(self.size)
        print(self.bounds)
        print(self.view.frame)
        center = self.size/2
        print(center)
        self.background_color = 'gray'
        self.sprite_label = 'dog'
        self.sprite = scene.SpriteNode('Dog_Face',
            position=(0, 400),
            anchor_point=(0, 1),
            #position=(0, 300),
            #anchor_point=(0, 0),
            #position=(400, 400),
            #anchor_point=(1, 1),
            ##position=(400, 200),
            #anchor_point=(1, 0),
            parent=self)
        print(self.sprite.position)
        self.label_node = scene.LabelNode('Hello World', 
            #position=(0, 400),
            #anchor_point=(0, 1),
            position=(0, 300),
            anchor_point=(0, 0),
            #position=(400, 400),
            #anchor_point=(1, 1),
            ##position=(400, 200),
            #anchor_point=(1, 0),
            parent=self)
            
    def update(self):
        global img_label      
        if self.sprite_label != img_label:
            if img_label == 'dog':
                self.sprite_label = 'dog'
                self.sprite.texture = scene.Texture('Dog_Face')
            else:
                self.sprite_label = 'cat'
                self.sprite.texture = scene.Texture('Cat_Face')
                       
v = ui.load_view()
frame = v.frame
scene_view = scene.SceneView()
#scene_view.flex= 'WH'
scene_view.width = frame.w
scene_view.height = frame.h
scene_view.scene = MyScene()
v['view1'].add_subview(scene_view)
print('bb',v['view1'].frame)
v.present('sheet')
