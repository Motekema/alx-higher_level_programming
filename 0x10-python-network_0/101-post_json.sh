#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
