#!/bin/bash
# Sends a POST request, displays response body, sends email, subject variables
curl -sX POST -d 'email=hr@holbertonschool.com&subject="I will always be here for PLD"' "$1"
