import editor, re, console, clipboard, os

path = editor.get_path()
#path = '~/Documents'+re.split('Documents', path)[1]
print(path)
clipboard.set(path)
console.hud_alert(path)
