#!/bin/bash
# take a URL, send request to it, and display size of body of response.
curl -sI "$1" | grep "Content-Length:" | cut -d ' ' -f2 | sed -e "s/[^0-9]//g"
