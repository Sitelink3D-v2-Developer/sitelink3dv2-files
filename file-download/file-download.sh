#!/bin/bash
# Shell file to download file.

## Settings for the site:
env="qa"
dc="us"
siteid=""

file_uuid=""

## Authentication
jwt=""
# - or -
oauth_id=""
oauth_secret=""
oauth_scope=""

exec python file-download.py \
    --dc "$dc" \
    --env "$env" \
    --siteid "$siteid" \
    --file-uuid "$file_uuid" \
    --jwt "$jwt" \
    --oauth-id "$oauth_id" \
    --oauth-secret "$oauth_secret" \
    --oauth-scope "$oauth_scope"