#!/bin/bash
# take a URL, send GET request, display only body of a 200 status code response
curl "$1" -sL
