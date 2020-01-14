#!/usr/bin/python3
# take in URL and email, send a POST req with email as param, display resp/utf8
from urllib import request
from urllib import parse
from urllib import error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            headers = response.info().items()
            html = response.read()
            utf8 = html.decode('UTF-8')
            print(utf8)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
