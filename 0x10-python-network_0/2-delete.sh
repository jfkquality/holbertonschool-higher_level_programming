#!/bin/bash
# send DELETE request to the URL passed and displays the body of the response
curl -s -X DELETE -d "I\'m a DELETE request" "$1"
