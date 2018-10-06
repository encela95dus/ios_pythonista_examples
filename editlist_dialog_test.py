

import dialogs


#lst = range(10)
lst = ['a'+str(i) for i in range(5)]
res = dialogs.edit_list_dialog('Please select', lst)
print(res)
