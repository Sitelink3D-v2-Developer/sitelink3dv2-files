@echo off
rem # Batch file to create a site.

rem ## Settings for the site:
set env="qa"
set dc="us"
set site_id=""

set file_uuid=""

rem ## Authentication
set jwt=""
rem # - or -
set oauth_id=""
set oauth_secret=""
set oauth_scope=""

python file-upload.py ^
    --dc %dc% ^
    --env %env% ^
    --site_id %site_id% ^
    --jwt %jwt% ^
    --oauth-id %oauth_id% ^
    --oauth-secret %oauth_secret% ^
    --oauth-scope %oauth_scope% ^
    file_uuid
