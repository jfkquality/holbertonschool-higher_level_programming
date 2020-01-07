#!/bin/bash
# take a URL, send GET request, display only body of a 200 status code response
curl -sIL "$1" | grep "200 OK" | cut -d ' ' -f 3-
