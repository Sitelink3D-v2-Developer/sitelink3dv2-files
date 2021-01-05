#!/bin/bash
# Shell file to upload file

## Settings for the site:
env="qa"
dc="us"
siteid=""

file_uuid=""
folder_uuid=""
file_path=""

## Authentication
jwt=""
# - or -
oauth_id=""
oauth_secret=""
oauth_scope=""

exec python file-upload.py \
    --dc "$dc" \
    --env "$env" \
    --siteid "$siteid" \
    --file-uuid "$file_uuid" \
    --file-path "$file_path" \
    --folder-uuid "$folder_uuid" \
    --jwt "$jwt" \
    --oauth-id "$oauth_id" \
    --oauth-secret "$oauth_secret" \
    --oauth-scope "$oauth_scope"