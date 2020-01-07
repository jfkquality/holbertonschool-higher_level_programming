#!/bin/bash
# request to 0.0.0.0:5000/catch_me, responds with a message  You got me!
curl -sL -X PUT 0.0.0.0:5000/catch_me -d 'user_id=98'
