import appex
import console, clipboard
import requests

def download_binary_file(url):
    if not url.startswith('http'):
        console.hud_alert('url error:' + url) 
        return None
    local_filename = (url.split('/')[-1]).split('?')[0]
    if not local_filename:
        local_filename = 'tmpfile.dat'
    with open(local_filename, 'wb') as f:
        try:
            r = requests.get(url, stream=True)
            total_length = r.headers.get('content-length')
            if not total_length:
                f.write(r.content)
            else:
                dl = 0
                total_length = float(total_length)
                for chunk in r.iter_content(1024):
                    dl += len(chunk)
                    f.write(chunk)
        except requests.exceptions.RequestException as e:
            console.hud_alert('requests error') 
            return None
    return local_filename

def main():
    if not appex.is_running_extension():
        url = clipboard.get()
        console.hud_alert('from clipboard url: ' + url)
    else:
        url = appex.get_url()
        if not url:
            console.hud_alert('no url')
            url = clipboard.get()
            console.hud_alert('from clipboard url: ' + url)
        else:
            console.hud_alert('from appex url: ' + url)
    local_filename = download_binary_file(url)
    if local_filename:
        console.hud_alert('copying to ' + local_filename)
        if (local_filename.endswith('.mp4') or 
            local_filename.endswith('.jpg') or
            local_filename.endswith('.jpeg') or
            local_filename.endswith('.png') or 
            local_filename.endswith('.gif') ):
            console.quicklook(local_filename)

if __name__ == '__main__':
    main()
