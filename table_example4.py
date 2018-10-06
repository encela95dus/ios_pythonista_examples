import ui

def make_cell(rowcolor, rowdata, cell_type = 'subtitle'):
    #TableViewCell params None,subtitle,value1,value2
    cell = ui.TableViewCell(cell_type)
    btn = ui.ImageView()
    btn.image = ui.Image('Dog_Face')
    btn.width = btn.height = 28
    
    btn.x, btn.y = 8 , (cell.height / 2) - (btn.height / 2)
    
    btn.background_color = rowcolor
    cell.content_view.add_subview(btn)
    cell.text_label.text = ' ' * 6 + rowdata
    cell.detail_text_label.text = ' ' * 9 + rowcolor
        
    return cell

def table_tapped(elem):
    section, row, rowdata, rowcolor = elem
    print(section, row, rowdata, rowcolor)

class MyTableViewDataSource(object):
    def __init__(self):
        self.data = ['aa', 'bb', 'cc', 'dd']
        self.colors = ['red', 'blue', 'green', 'orange']
        
    def tableview_number_of_sections(self, tableview):
        # Return the number of sections (defaults to 1)
        return 1

    def tableview_number_of_rows(self, tableview, section):
        # Return the number of rows in the section
        return len(self.data) 

    def tableview_cell_for_row(self, tableview, section, row):
        # Create and return a cell for the given section/row
        return make_cell(self.colors[row], self.data[row])
        
    def tableview_title_for_header(self, tableview, section):
        # Return a title for the given section.
        # If this is not implemented, no section headers will be shown
        if section == 0:
            return 'Color table'
                
    def tableview_did_select(self, tableview, section, row):
        if section == 0:
            table_tapped((section, row, self.data[row], self.colors[row]))
            
                
datasource = MyTableViewDataSource()
datasource.action = table_tapped
tv = ui.TableView(frame=(0,0, 400, 400))
tv.data_source = tv.delegate = datasource

tv.present('sheet')
