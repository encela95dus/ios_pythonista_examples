# coding: utf-8
import editor
import ui

def main():
    html = editor.get_text()
    if not html:
        print('No input text found. Use this script from the share sheet in an app like Notes.')
        return
    webview = ui.WebView(name='Html Preview')
    webview.load_html(html)
    webview.present()

if __name__ == '__main__':
    main()

