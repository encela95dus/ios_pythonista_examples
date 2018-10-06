from PIL import Image, ImageOps
import appex
import ui, clipboard, console

def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    img = appex.get_image()
    if not img:
        print('No input image')
        return
    if not img.mode.startswith('RGB'):
        img = img.convert('RGB')
    gray_img = ImageOps.grayscale(img)
    clipboard.set_image(gray_img)

console.hud_alert('processing')
console.show_activity()
main()
console.hud_alert(' complete')
console.hide_activity()
appex.finish()
