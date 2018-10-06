import ui

def table_tapped(sender):
    rowtext = sender.items[sender.selected_row]
    print(rowtext)

datasource = ui.ListDataSource(range(20))
datasource.action = table_tapped
v = ui.load_view()
tv = v['tableview1']
tv.data_source = tv.delegate = datasource
v.present('sheet')

