#!/bin/bash
# Shell file to create a site.

## Settings for the site:
env="qa"
dc="us"
site_id=""

folder_name="New Folder"
folder_uuid=
parent_uuid=

## Authentication
jwt=""
# - or -
oauth_id=""
oauth_secret=""
oauth_scope=""


exec python make-folder.py \
    --dc "$dc" \
    --env "$env" \
    --site-id "$site_id" \
    --folder-uuid "$folder_uuid" \
    --parent-uuid "$parent_uuid" \
    --jwt "$jwt" \
    --oauth-id "$oauth_id" \
    --oauth-secret "$oauth_secret" \
    --oauth-scope "$oauth_scope" \
    "$folder_name"
