#!/bin/bash
# take a URL, send GET request, display only body of a 200 status code response
curl -sI "$1" | head -1 | cut -d ' ' --complement -f1-2
