#!/bin/bash
# This script takes a URL as an argument, sends a request, and displays only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
