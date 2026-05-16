import urllib.request
import json
import re

try:
    html = urllib.request.urlopen('https://www.youtube.com/@dhyutifrontiers').read().decode('utf-8')
    match = re.search(r'"externalId":"(UC[a-zA-Z0-9_-]+)"', html)
    if match:
        print("externalId:", match.group(1))
    else:
        match2 = re.search(r'"channelId":"(UC[a-zA-Z0-9_-]+)"', html)
        if match2:
            print("channelId:", match2.group(1))
        else:
            print("Not found")
            # Dump a snippet to see what's there
            idx = html.find('channelId')
            if idx != -1:
                print(html[idx:idx+100])
except Exception as e:
    print("Error:", e)
