#!/usr/bin/python3
# sends a request to URL with mailto. display emailto in the response header
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    r = requests.post(url, data=email)
    print(r.text)
