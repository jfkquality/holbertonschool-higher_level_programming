#!/bin/bash
# JSON POST req, display response. send POST w file passed as 2nd arg of script
curl -s -X POST "$1" -H "Content-Type: application/json" -d "@${2}"
