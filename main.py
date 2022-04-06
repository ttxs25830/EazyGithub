import re
import time
import requests
import os

hostpath = "C:\Windows\System32\drivers\etc\hosts"
addressurl = "https://raw.hellogithub.com/hosts"

def gethost():
    raw = ""
    while True:
        try:
            raw = requests.get(url=addressurl)
            raw.raise_for_status()
        except:
            time.sleep(1)
        else:
            break
    return raw.text

host = ""
with open(hostpath, 'r', encoding='UTF-8') as fhost:
    host = fhost.read()
host = re.sub(r'# GitHub520 Host Start[\s\S]+?# GitHub520 Host End\n', "", host)+gethost()
with open(hostpath, 'w', encoding='UTF-8') as fhost:
    fhost.write(host)