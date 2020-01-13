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
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(utf8))
