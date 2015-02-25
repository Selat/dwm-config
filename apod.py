#!/usr/bin/env python3

import urllib.request, re, os, time

apod_url = 'http://apod.nasa.gov/apod/'

def get_picture_url(url):
    """Download page from the url and return it's body."""
    with urllib.request.urlopen(url) as f:
        data = f.read().decode('utf-8')
    s = re.search(r'href=[\'"]?image([^\'" >]+)', data).group(0)
    return url + s[6:len(s)]

def download_picture(url):
    urllib.request.urlretrieve(get_picture_url(url), "background.jpg")

if __name__ == '__main__':
    should_download = True
    if os.path.exists("background.jpg"):
        modified_time = time.gmtime(os.path.getmtime("background.jpg"))
        cur_time = time.gmtime()
        if modified_time.tm_year == cur_time.tm_year and modified_time.tm_yday == cur_time.tm_yday:
            should_download = False

    if should_download:
        download_picture(apod_url)
    os.system("feh --bg-center background.jpg")
