import dialogs
import datetime

form_list_of_sections = []

sectionA_dicts = []
sectionA_dicts.append(dict(type = 'text', title = 'First Name',
key = 'first', placeholder = 'John'))

sectionA_dicts.append(dict(type = 'text', title = 'Last Name',
key = 'last', placeholder = 'Doe')) 

sectionA_dicts.append(dict(type = 'number', title = 'age',
key = 'age', placeholder='30')) 

form_list_of_sections.append(('Section A', sectionA_dicts, 'Section A ends'))

sectionB_dicts = []
sectionB_dicts.append(dict(type = 'date', title = 'Date Of Birth',
key = 'DOB', value = datetime.date.today()))

sectionB_dicts.append(dict(type = 'url', title = 'Home Page',
    key = 'homepage', placeholder = 'http://example.com')) 
    
form_list_of_sections.append(('Section B', sectionB_dicts, 'Section B ends'))

sectionC_dicts = []
sectionC_dicts.append(dict(type = 'email', title = 'email',
key = 'email', placeholder = 'name@mailserver.com')) 

sectionC_dicts.append(dict(type = 'switch', title = 'is_married',
key = 'is_married', value = True))  

sectionC_dicts.append(dict(type = 'check', title = 'is_registered',
key = 'is_registered', value = False))  

form_list_of_sections.append(('Section C', sectionC_dicts, 'Section C ends'))

diag = dialogs.form_dialog(title = 'Form Dialog', sections=form_list_of_sections)
print(diag)
