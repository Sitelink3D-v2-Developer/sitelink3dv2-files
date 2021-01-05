#!/bin/bash
# Shell file to create a site.

## Settings for the site:
env="qa"
dc="us"
siteid=""

folder_name=""
folder_uuid=""
parent_uuid=""

## Authentication
jwt=""
# - or -
oauth_id=""
oauth_secret=""
oauth_scope=""


exec python make-folder.py \
    --dc "$dc" \
    --env "$env" \
    --siteid "$siteid" \
    --folder-name "$folder_name" \
    --folder-uuid "$folder_uuid" \
    --parent-uuid "$parent_uuid" \
    --jwt "$jwt" \
    --oauth-id "$oauth_id" \
    --oauth-secret "$oauth_secret" \
    --oauth-scope "$oauth_scope"