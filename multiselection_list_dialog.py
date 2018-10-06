import dialogs

def multiple_selection_list_dialog(lst):
    form_list_of_dicts = []
    for item in lst:
        form_list_of_dicts.append(dict(type = 'check', title = item,
            key = item, value = False))  
    result = dialogs.form_dialog(title = 'Multiple Selection List', fields=form_list_of_dicts) 
    return [i for i in result if result[i]] if result else None

if __name__ == '__main__':
    lst = ['a'+str(i) for i in range(5)]
    print(multiple_selection_list_dialog(lst))
