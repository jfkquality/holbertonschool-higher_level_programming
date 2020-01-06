#!/bin/bash
# take a URL, send GET request, display only body of a 200 status code response
curl -sI "$1" | grep "Content-Length:" | cut -d ' ' --complement -f1-2
