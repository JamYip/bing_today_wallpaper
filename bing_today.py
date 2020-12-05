import requests
import subprocess
import os
import json
import time

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}

def getImgUrl():
    query_url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    root_url = "https://www.bing.com"
    r = requests.get(query_url, headers = headers)
    respond_json = json.loads(r.text)
    img_url_base = respond_json.get('images')[0].get('urlbase')
    img_url = root_url + img_url_base + '_UHD.jpg'
    return img_url

def downloadImg(url, path):
    r = requests.get(url, headers = headers)
    with open(path, 'wb') as f:
        f.write(r.content)

def setWallpaper(path):
    script = 'tell application "Finder" to set desktop picture to POSIX file "' + path + '"'
    proc = subprocess.Popen(['osascript', '-'],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    stdout, stderr = proc.communicate(script)

def makePath():
    path = os.environ['HOME'] + '/' + 'Pictures/bing/'
    if os.path.exists(path) == False:
        os.makedirs(path)
    path = path + time.strftime('%Y%m%d.jpg')
    return path


if (__name__ == "__main__"):
    url = getImgUrl()
    path = makePath()
    downloadImg(url, path)
    setWallpaper(path)