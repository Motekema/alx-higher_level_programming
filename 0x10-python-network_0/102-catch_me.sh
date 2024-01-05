#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me causing the server
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
