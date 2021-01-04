#!/bin/bash
# Shell file to download file.

## Settings for the site:
env="qa"
dc="us"
site_id=""

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
    --site-id "$site_id" \
    --jwt "$jwt" \
    --oauth-id "$oauth_id" \
    --oauth-secret "$oauth_secret" \
    --oauth-scope "$oauth_scope" \
    "$file_uuid"
