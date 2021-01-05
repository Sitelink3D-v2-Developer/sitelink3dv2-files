@echo off
rem # Batch file to create a site.

rem ## Settings for the site:
set env="qa"
set dc="us"
set siteid=""

set limit="20"
rem ## uuid
set start=""


rem ## Authentication
set jwt=""
rem # - or -
set oauth_id=""
set oauth_secret=""
set oauth_scope=""

python file-listing.py ^
    --dc %dc% ^
    --env %env% ^
    --siteid %siteid% ^
    --start %start% ^
    --limit %limit% ^
    --jwt %jwt% ^
    --oauth-id %oauth_id% ^
    --oauth-secret %oauth_secret% ^
    --oauth-scope %oauth_scope%
