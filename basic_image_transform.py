from PIL import Image, ImageOps, ImageFilter
import ui

def sketch(img):
    edge_img = img.filter(ImageFilter.CONTOUR)
    return ImageOps.grayscale(edge_img)

def emboss(img):
    edge_img = img.filter(ImageFilter.EMBOSS)
    return ImageOps.grayscale(edge_img)

import io

def ui2pil(ui_img):
    return Image.open(io.BytesIO(ui_img.to_png()))

def pil2ui(pil_img):
    with io.BytesIO() as buffer:
        pil_img.save(buffer, format='PNG')
        return ui.Image.from_data(buffer.getvalue())

def main():
    pilimg = ui.Image.named('Dog_Face')
    img = ui2pil(pilimg)
    sketch(img).show()
    img1 = pil2ui(img)
    img2 = ui2pil(img1)
    emboss(img2).show()

if __name__ == '__main__':
    main()




