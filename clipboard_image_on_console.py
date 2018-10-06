import ui, clipboard, console

img = clipboard.get_image()
if img:
    img.show()
else:
    print('No image in the clipboard')


