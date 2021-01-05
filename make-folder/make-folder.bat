@echo off
rem # Batch file to create a site.

rem ## Settings for the site:
set env="qa"
set dc="us"
set siteid=""

set folder_name=""
set folder_uuid=""
set parent_uuid=""

rem ## Authentication
set jwt=""
rem # - or -
set oauth_id=""
set oauth_secret=""
set oauth_scope=""

python make-folder.py ^
    --dc %dc% ^
    --env %env% ^
    --siteid %siteid% ^
    --folder-name %folder_name% ^
    --folder-uuid %folder_uuid% ^
    --parent-uuid %parent_uuid% ^
    --jwt %jwt% ^
    --oauth-id %oauth_id% ^
    --oauth-secret %oauth_secret% ^
    --oauth-scope %oauth_scope%