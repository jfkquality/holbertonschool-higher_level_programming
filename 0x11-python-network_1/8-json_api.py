#!/usr/bin/python3
# sends a request to URL with mailto. display emailto in the response header
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if not argv[1]:
        q = ""
    else:
        q = argv[1]
    q = {'letter': argv[1]}
    r = requests.post(url, data = q)
    if r.headers['Content-Type'] = 'application/json':
        print("[{}], {}".format(r.id, r.name))
    elif not r.headers:
        print("No result")
    else:
        print("Not a vaild JSON")
