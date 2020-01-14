#!/usr/bin/python3
# sends a request to URL argv, display X-Request-Id in the response header
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
