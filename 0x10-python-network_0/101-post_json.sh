#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response. The JSON content is read from a file
# passed as the second argument.

file_content=$(cat "$2")

if jq -e . >/dev/null 2>&1 <<<"$file_content"; then
    curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
else
    echo "Not a valid JSON"
fi
