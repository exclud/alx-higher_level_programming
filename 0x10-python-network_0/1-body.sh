#!/bin/bash
# This script takes a URL as an argument, sends a GET request, and displays the body of the response for a 200 status code.
curl -sL "$1"
