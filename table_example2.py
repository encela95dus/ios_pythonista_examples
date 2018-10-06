import ui

def edit_action(sender):
    tv = sender.superview['tableview1']
    tv.editing = True
    tv.data_source.move_enabled = True
    tv.reload_data()

def done_action(sender):
    tv = sender.superview['tableview1']
    tv.editing = False
    tv.data_source.move_enabled = False
    tv.reload_data()


def table_tapped(sender):
    rowtext = sender.items[sender.selected_row]
    print(rowtext)

datasource = ui.ListDataSource(range(20))
datasource.action = table_tapped
v = ui.load_view()
tv = v['tableview1']
tv.data_source = tv.delegate = datasource
v.present('sheet')

