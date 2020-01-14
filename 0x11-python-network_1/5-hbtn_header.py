#!/usr/bin/python3
# fetch https://intranet.hbtn.io/status. You must use the package requests
import requests
from sys import argv

url = argv[1]
r = requests.get(url)
print(r.headers['X-Request-Id'])
