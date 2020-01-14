#!/usr/bin/python3
# sends a request to URL argv, display X-Request-Id in the response header
import requests
from sys import argv

url = argv[1]
r = requests.get(url)
print(r.headers['X-Request-Id'])
