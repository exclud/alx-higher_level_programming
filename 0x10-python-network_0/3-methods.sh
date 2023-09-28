#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accept.
curl -sI --head "$1" | grep -i 'Allow' | cut -d " " -f 2-
