#!/bin/bash
# take a URL, send GET request, display only body of a 200 status code response
curl  "$1" -sLI | grep "200 OK" | sed -e "s/[^a-zA-Z0-9.// ]//g"  #| cut -d ' ' -f2-
