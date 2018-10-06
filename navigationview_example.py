import ui

def add_close_buttonitem(v):
    close = ui.ButtonItem()
    close.image = ui.Image.named('ionicons-close-24')
    close.action = bt_close
    v.left_button_items = [close]

def add_right_buttonitem(v, action):
    right = ui.ButtonItem()
    right.image = ui.Image.named('ionicons-arrow-right-b-24')
    right.action = action
    v.right_button_items = [right]  

def bt_subview2(sender):
    sub_view = ui.load_view('navtest_subview2')
    nav_view.push_view(sub_view)

def bt_subview1(sender):
    sub_view = ui.load_view('navtest_subview1')
    add_right_buttonitem(sub_view, bt_subview2)
    nav_view.push_view(sub_view)
    
def bt_close(sender):
    nav_view.close()


main_view = ui.load_view('navtest_mainview')
add_close_buttonitem(main_view)
add_right_buttonitem(main_view, bt_subview1)

nav_view = ui.NavigationView(main_view)
nav_view.width = 600
nav_view.height = 400
nav_view.present("sheet",  hide_title_bar=True)

