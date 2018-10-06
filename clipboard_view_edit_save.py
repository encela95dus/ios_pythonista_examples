import dialogs, clipboard

txt = clipboard.get()
edited_text = dialogs.text_dialog(
    title='View and edit clipboard text',
    text=txt)
if edited_text != txt:
    clipboard.set(edited_text)
#dialogs.share_text(clipboard.get())
