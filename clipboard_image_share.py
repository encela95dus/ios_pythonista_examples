import ui, dialogs, clipboard
img = ui.Image('Dog_Face')
clipboard.set_image(img)
dialogs.share_image(clipboard.get_image()) 
