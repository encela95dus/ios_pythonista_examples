# coding: utf-8

# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
import editor
from markdown2 import markdown
import ui

TEMPLATE = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title>Preview</title>
<style type="text/css">
body {
        font-family: helvetica;
        font-size: 15px;
        margin: 10px;
}
</style>
</head>
<body>{{CONTENT}}</body>
</html>
'''

def main():
    text = editor.get_text()
    if not text:
        print('No input text found. Use this script from the share sheet in an app like Notes.')
        return
    converted = markdown(text)
    html = TEMPLATE.replace('{{CONTENT}}', converted)
    webview = ui.WebView(name='Markdown Preview')
    webview.load_html(html)
    webview.present()

if __name__ == '__main__':
    main()

