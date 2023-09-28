#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me to get the server response without displaying it directly.
curl -sL -X PUT -H "Origin: You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me
