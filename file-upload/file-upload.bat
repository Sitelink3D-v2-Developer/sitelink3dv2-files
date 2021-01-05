@echo off
rem # Batch file to create a site.

rem ## Settings for the site:
set env="qa"
set dc="us"
set siteid=""

set file_uuid=""
set folder_uuid=""
set file_path=""

rem ## Authentication
set jwt=""
rem # - or -
set oauth_id=""
set oauth_secret=""
set oauth_scope=""

python file-upload.py ^
    --dc %dc% ^
    --env %env% ^
    --siteid %siteid% ^
    --file-uuid %file_uuid% ^
    --file-path %file_path% ^
    --folder-uuid %folder_uuid% ^
    --jwt %jwt% ^
    --oauth-id %oauth_id% ^
    --oauth-secret %oauth_secret% ^
    --oauth-scope %oauth_scope%
