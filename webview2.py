import ui
import os

file_path = os.path.abspath('matrix.html')
v = ui.WebView(frame=(0,0,400,400), name='Matrix Display')
v.load_url('File://'+file_path)
v.present('sheet')

