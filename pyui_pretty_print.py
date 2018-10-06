import json, pprint, editor, console

def file_selection_dialog(dir_path='.'):
    import dialogs
    import os
    def files_and_folders(dir_path='.'):
        '''Return a dict containing a sorted tuple of files and a sorted
        tuple of folders'''
        f_and_f = os.listdir(dir_path)
        folders = [f for f in f_and_f if os.path.isdir(os.path.abspath(f))]
        all_files = set(f_and_f) - set(folders)
        files = [i for i in all_files if i.endswith('.pyui') ] # only pyui files      
        return (tuple(sorted(files, key=str.lower)),
                tuple(sorted(folders, key=str.lower)))
    files, folders = files_and_folders(dir_path=dir_path)
    items = []
    if os.path.abspath(dir_path) != os.path.expanduser('~/Documents'):
        items.append({'title': '..',
                      'image': 'ionicons-arrow-up-c-32'})
    items += [{'title':i,
               'image':'ionicons-folder-32',
               'accessory_type': 'disclosure_indicator',
               'is_dir': True} for i in folders] + [
              {'title':i,
               'image':'ionicons-document-text-32',
               'accessory_type': 'none',
               'is_dir': False} for i in files]     
    result = dialogs.list_dialog('Select File', items)
    if result:
        if result['title'] == '..':
            os.chdir('..')
            result = file_selection_dialog()
        elif result['is_dir']:
            os.chdir(result['title'])
            result = file_selection_dialog()
        return result
    else:
        return None

if __name__ == '__main__':
    import os
    result = file_selection_dialog()
    #print(os.path.abspath(result['title']) if result else None)
    path = os.path.abspath(result['title']) if result else None
    if path and path.endswith('.pyui'):
        with open(path) as in_file:
            pprint.pprint(json.load(in_file))
    else:
        console.hud_alert('file selected is not pyui file')
