#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep -Fi Allow | cut -d ' ' -f2-  # | sed -e "s/[^0-9]//g"
