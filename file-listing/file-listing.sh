#!/bin/bash
# Shell file to list files

## Settings for the site:
env="qa"
dc="us"
site_id=""

limit="20"
# start id uuid
start=

## Authentication
jwt=""
# - or -
oauth_id=""
oauth_secret=""
oauth_scope=""

exec python file-listing.py \
    --dc "$dc" \
    --env "$env" \
    --site-id "$site_id" \
    --start "$start" \
    --limit "$limit" \
    --jwt "$jwt" \
    --oauth-id "$oauth_id" \
    --oauth-secret "$oauth_secret" \
    --oauth-scope "$oauth_scope"
