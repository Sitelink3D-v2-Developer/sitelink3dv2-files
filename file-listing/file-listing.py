#!/usr/bin/python
import argparse
import json
import logging
import os
import sys
import requests
import base64

sys.path.append("../utils")
from utils import *

# >> Environment settings:
settings = {
    "SR_EDGE_DC": "us",
    "SR_EDGE_SCHEME": "http",
    "SR_EDGE_HOST": "sr-edge",
    "SR_EDGE_PORT": "9094",
    "AUTH_TOKEN": "",
}
for setting in settings:
    globals()[setting] = os.getenv(setting, settings[setting])
# << Environment settings


# >> Arguments
arg_parser = argparse.ArgumentParser(description="Files Listing")

# script parameters:
arg_parser.add_argument("--log-format", default='%(asctime)-15s %(module)s %(levelname)s %(funcName)s %(message)s')
arg_parser.add_argument("--log-level", default=logging.INFO)

# server parameters:
arg_parser.add_argument("--dc", default="SR_EDGE_DC", required=True)
arg_parser.add_argument("--env", default="", help="deploy env (which determines server location)")
arg_parser.add_argument("--jwt", default=AUTH_TOKEN, help="jwt")
arg_parser.add_argument("--oauth-id", default="", help="oauth-id")
arg_parser.add_argument("--oauth-secret", default="", help="oauth-secret")
arg_parser.add_argument("--oauth-scope", default="", help="oauth-scope")

# request parameters:
arg_parser.add_argument("--site-id", default="", help="Site Identifier", required=True)
arg_parser.add_argument("--start", default="", help="Start from here")
arg_parser.add_argument("--limit", default="10", help="Page size")

arg_parser.set_defaults()
args = arg_parser.parse_args()
logging.basicConfig(format=args.log_format, level=args.log_level)
# << Arguments


# << Server settings
scheme, host, port = shp(args.env, SR_EDGE_SCHEME, SR_EDGE_HOST, SR_EDGE_PORT)
server_url = "{}://{}-{}:{}".format(scheme, args.dc, host, port)
rdm_list_files_url = "{0}/rdm/v1/site/{1}/domain/{2}/view/{3}".format(server_url, args.site_id, "file_system", "v_fs_files_by_folder")
oauth_edge_url = "{0}/oauth/v1/token".format(server_url)
headers = {'content-type': 'application/json', 'X-Topcon-Auth' : args.jwt}
session = requests.Session()
if args.env == "local":
    session.verify = False
if len(args.oauth_id) > 0 and len(args.oauth_secret) > 0 and len(args.oauth_scope) > 0:
    # get oauth token
    headers = get_oauth_header(oauth_edge_url, args.oauth_id, args.oauth_secret, args.oauth_scope)
# << Server settings

# Listing files
params = {}
if len(args.limit) > 0:
    params["limit"] = args.limit
if len(args.start) > 0:
    s_id = json.dumps([args.start]).encode()
    params["start"] = base64.urlsafe_b64encode(s_id).replace("=", "", 4)

response = session.get(rdm_list_files_url, headers=headers, params=params)
response.raise_for_status()

print ("Files listing result for site {0} \n{1}".format(args.site_id, json.dumps(response.json(), indent=4)))
