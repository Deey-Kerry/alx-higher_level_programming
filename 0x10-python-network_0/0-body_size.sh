#!/usr/bin/python3
#sends a request to that URL, and displays the size of the response
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r'
