#!/bin/bash
# send request to URL and displays only the status code of the response.
curl -sI -o /dev/null -w "%{http_code}" "$1"
