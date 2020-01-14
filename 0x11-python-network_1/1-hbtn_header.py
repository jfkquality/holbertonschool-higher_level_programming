#!/usr/bin/python3
# send request to URL and display value of X-Request-Id variable in the headef

import urllib.request
import sys

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        headers = response.info().items()
    for line in headers:
        if line[0] == "X-Request-Id":
            print(line[1])
