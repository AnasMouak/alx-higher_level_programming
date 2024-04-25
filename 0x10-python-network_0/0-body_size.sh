#!/bin/bash
#script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -X GET -o /dev/null -w "%{size_download}\n" "$1"
