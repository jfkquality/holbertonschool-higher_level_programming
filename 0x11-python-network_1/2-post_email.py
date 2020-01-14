#!/usr/bin/python3
# take in URL and email, send a POST req with email as param, display resp/utf8
from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    email = {'email': argv[2]}
    email = parse.urlencode(email)
    email = data.encode('ascii')
    req = request.Request(url, email)
    with request.urlopen(req) as response:
        headers = response.info().items()
        html = response.read()
        utf8 = html.decode('UTF-8')
    print(utf8)
