#!/usr/bin/python3
# Fetches https://intranet.hbtn.io/status
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    # req = urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        html = response.read()
        utf8 = html.decode('UTF-8')
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(utf8))
