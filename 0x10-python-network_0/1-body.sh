#!/bin/bash
# take a URL, send GET request, display only body of a 200 status code response
curl -sIL "$1" | grep "HTTP/1.0 200" | cut -d ' ' -f3-
