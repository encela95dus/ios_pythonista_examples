import ui, photos


def get_image_from_photos(sender):
    v = sender.superview
    img1 = photos.pick_asset(assets=photos.get_assets(media_type='image')).get_ui_image()
    w,h = img1.size
    img_view = ui.ImageView(frame=(0,0,w,h), name='imageview1', image=img1)
    v['scrollview1'].remove_subview(v['scrollview1']['imageview1'])
    v['scrollview1'].content_size = w,h
    v['scrollview1'].add_subview(img_view)
    
def get_stored_image(sender):
    v = sender.superview
    img1 = stored_image
    w,h = img1.size
    img_view = ui.ImageView(frame=(0,0,w,h), name='imageview1', image=img1)
    v['scrollview1'].remove_subview(v['scrollview1']['imageview1'])
    v['scrollview1'].content_size = w,h
    v['scrollview1'].add_subview(img_view)

v = ui.load_view()
#stored_image = ui.Image('pythonista_logo.png') # png file in current directory
stored_image = ui.Image('test:Mandrill')
w,h = stored_image.size
img_view = ui.ImageView(frame=(0,0,w,h), name='imageview1', image=stored_image)
v['scrollview1'].content_size = w,h
v['scrollview1'].add_subview(img_view)
v.present('sheet')
