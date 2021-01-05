#!/usr/bin/python
import argparse
import logging
import os
import sys
import requests
import json
import base64
import uuid
import time

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
arg_parser = argparse.ArgumentParser(description="Creating a Directory")

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
arg_parser.add_argument("--siteid", default="", help="Site Identifier", required=True)
arg_parser.add_argument("--folder-name", default="New Folder", help="Name for new folder")
arg_parser.add_argument("--folder-uuid", default=str(uuid.uuid4()), help="UUID of folder")
arg_parser.add_argument("--parent-uuid", default=None, help="UUID of parent")

arg_parser.set_defaults()
args = arg_parser.parse_args()
logging.basicConfig(format=args.log_format, level=args.log_level)
# << Arguments


# << Server settings
scheme, host, port = shp(args.env, SR_EDGE_SCHEME, SR_EDGE_HOST, SR_EDGE_PORT)
server_url = "{}://{}-{}:{}".format(scheme, args.dc, host, port)
rdm_create_folder_url = "{0}/rdm_log/v1/site/{1}/domain/{2}/events".format(server_url, args.siteid, "file_system")
oauth_edge_url = "{0}/oauth/v1/token".format(server_url)
session = requests.Session()
if args.env == "local":
    session.verify = False
headers = {'content-type': 'application/json', 'X-Topcon-Auth': args.jwt}
if len(args.oauth_id) > 0 and len(args.oauth_secret) > 0 and len(args.oauth_scope) > 0:
    # get oauth token
    headers = get_oauth_header(oauth_edge_url, args.oauth_id, args.oauth_secret, args.oauth_scope)
# << Server settings

# Create Folder
payload = {
    "_at"  : int(round(time.time() * 1000)),
    "_rev" : str(uuid.uuid4()),
    "_type": "fs::folder",
    "_v"   : 0,
    "name" : args.folder_name,
}
if is_valid_uuid(args.folder_uuid):
    payload["_id"] = args.folder_uuid
else:
    payload["_id"] = str(uuid.uuid4())

if is_valid_uuid(args.parent_uuid): payload["parent"] = args.parent_uuid

data_encoded_json = {"data_b64": base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')}
print (data_encoded_json)
response = session.post(rdm_create_folder_url, headers=headers, data=json.dumps(data_encoded_json))
print (response.text)
response.raise_for_status()
print ("make-folder returned {0}\n{1}".format(response.status_code, json.dumps(response.json(), indent=4)))
print ("The new folder uuid = {0}".format(payload["_id"]))
