#!/usr/bin/python3
# sends a request to URL argv, display X-Request-Id in the response header
import requests
from sys import argv

url = argv[1]
email = argv[2]
r = requests.post(url, data=email)
print(r.text)
