import ui, dialogs

def alert_action(sender):
    print(dialogs.alert('alert', 'test message', 'button1', 'button2'))

def input_alert_action(sender):
    print(dialogs.input_alert('input alert', 'test  message'))

def password_alert_action(sender):
    print(dialogs.password_alert('passwd alert'))

def login_alert_action(sender):
    print(dialogs.login_alert('login alert'))

def hudalert_action(sender):
    print(dialogs.hud_alert('hud alert message'))

def text_dialog_action(sender):
    print(dialogs.text_dialog('text dialog', text='Testing text dialog'))

def list_dialog_action(sender):
    print(dialogs.list_dialog('list dialog', items=[1,2,3,4]))

def edit_list_dialog_action(sender):
    print(dialogs.edit_list_dialog('edit list dialog', items=[1,2,3,4]))

def datetime_dialog_action(sender):
    print(dialogs.datetime_dialog('Datetime dialog'))

def date_dialog_action(sender):
    print(dialogs.date_dialog('Datetime dialog'))

def time_dialog_action(sender):
    print(dialogs.time_dialog('Datetime dialog'))

def duration_dialog_action(sender):
    print(dialogs.duration_dialog('Datetime dialog'))
    
    
v = ui.load_view()
v.present('sheet')
