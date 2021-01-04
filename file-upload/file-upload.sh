#!/bin/bash
# Shell file to upload file

## Settings for the site:
env="qa"
dc="us"
site_id=""

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
    --site-id "$site_id" \
    --file-uuid "$file_uuid" \
    --folder-uuid "$folder_uuid" \
    --jwt "$jwt" \
    --oauth-id "$oauth_id" \
    --oauth-secret "$oauth_secret" \
    --oauth-scope "$oauth_scope" \
    "$file_path"
