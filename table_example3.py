import ui

def table_tapped(sender):
    rowtext = sender.items[sender.selected_row]
    print(rowtext)


class MyTableViewDataSource(ui.ListDataSource):
    def __init__(self, items=None):
        super().__init__(items)
    def tableview_accessory_button_tapped(self, tableview, section, row):
        print(row)

data = ['aa', 'bb', 'cc', 'dd']
items = [  {'title':i,
            'image':'ionicons-folder-32',
            'accessory_type': 'checkmark'}  for i in data]
            #'accessory_type': 'detail_disclosure_button'}  for i in data]
            #'accessory_type': 'detail_button'}  for i in data]
            #'accessory_type': 'disclosure_indicator'}  for i in data]      
datasource = MyTableViewDataSource(items)
datasource.action = table_tapped
tv = ui.TableView(frame=(0,0, 400, 400))
tv.data_source = tv.delegate = datasource

tv.present('sheet')
