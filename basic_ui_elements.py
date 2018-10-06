import ui


def textfield_action(sender):
    sender.superview['label1'].text = 'Text Field:' + str(
        sender.superview['textfield1'].text)
        
def segmentedcontrol_action(sender):
    sc = sender.superview['segmentedcontrol1']
    segments_list = sc.segments
    selected_text = segments_list[sc.selected_index]
    sender.superview['label1'].text = 'Segmented Control:' + selected_text
    
def slider_action(sender):
    sender.superview['label1'].text = 'Slider:' + str(
        int(sender.superview['slider1'].value*100))

def datepicker_action(sender):
    sender.superview['label1'].text = 'Date:' + str(
        sender.superview['datepicker1'].date)   
             
def switch_action(sender):
    sender.superview['label1'].text = 'Switch:' + str(
        int(sender.superview['switch1'].value))

cnt = 0
def button_action(sender):
    global cnt
    cnt += 1
    sender.superview['label1'].text = 'Button Counter:' + str(cnt)

v = ui.load_view()
v.present('sheet')
