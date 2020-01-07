#!/bin/bash
# send request to URL and displays only the status code of the response.
# curl -sIL "$1" | grep -Fi "200 OK" | cut -d ' ' -f2
curl -sI -o /dev/null -w "%{http_code}" "$1"
