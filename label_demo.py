import ui

def make_label(text, font, alignment, background_color, x, y):
    w, h = ui.measure_string(text, 
                font=font, alignment=alignment, max_width=0)
    #print(w,h)
    label = ui.Label(text=text,
                font=font, alignment=alignment, 
                background_color=background_color, frame=(x,y,w,h), border_width=1)
    return label

v = ui.load_view()

v.add_subview(make_label(
    #'AajJpPyY iIlL', ('Helvetica', 80), ui.ALIGN_LEFT,
    #'AajJpPyY iIlL', ('TimesNewRomanPSMT', 80), ui.ALIGN_LEFT,   
    'AajJpPyY iIlL', ('Avenir-Roman', 80), ui.ALIGN_LEFT,         
    'lightgray', 30,350))
   
v.present('sheet')
