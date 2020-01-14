#!/usr/bin/python3
# send request to URL and display value of X-Request-Id variable in the headef

from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as response:
        headers = response.info().items()
    for line in headers:
        if line[0] == "X-Request-Id":
            print(line[1])
