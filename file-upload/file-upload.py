#!/usr/bin/python
import argparse
import json
import logging
import os
import sys
import requests
import time
import uuid

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
arg_parser = argparse.ArgumentParser(description="File Upload.")

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
arg_parser.add_argument("--file-path", help="File to upload")
arg_parser.add_argument("--file-uuid", default=str(uuid.uuid4()), help="File uuid")
arg_parser.add_argument("--folder-uuid", default=None, help="Folder uuid")

arg_parser.set_defaults()
args = arg_parser.parse_args()
logging.basicConfig(format=args.log_format, level=args.log_level)
# << Arguments

# << Server settings
scheme, host, port = shp(args.env, SR_EDGE_SCHEME, SR_EDGE_HOST, SR_EDGE_PORT)
server_url = "{}://{}-{}:{}".format(scheme, args.dc, host, port)
upload_file_url = "{0}/file/v1/sites/{1}/upload".format(server_url, args.siteid)
rdm_upload_url = "{0}/rdm_log/v1/site/{1}/domain/{2}/events".format(server_url, args.siteid, "file_system")
oauth_edge_url = "{0}/oauth/v1/token".format(server_url)
headers = {'content-type': 'application/json', 'X-Topcon-Auth': args.jwt}
session = requests.Session()
if args.env == "local":
    session.verify = False
if len(args.oauth_id) > 0 and len(args.oauth_secret) > 0 and len(args.oauth_scope) > 0:
    # get oauth token
    headers = get_oauth_header(oauth_edge_url, args.oauth_id, args.oauth_secret, args.oauth_scope)
# << Server settings

# Upload file
if is_valid_uuid(args.file_uuid):
    file_uuid = args.file_uuid
else:
    file_uuid = str(uuid.uuid4())

file_path = args.file_path
file_name = os.path.basename(file_path)
file_size = os.path.getsize(file_path)
params = {
    "upload-file-name": file_name,
    "upload-file-size": file_size,
    "upload-uuid": file_uuid,
}

with open(file_path, 'rb') as file_ptr:
    files = {
        "upload-file": file_ptr
    }
    if 'content-type' in headers:
        del headers['content-type']
    response = session.post(upload_file_url, headers=headers, params=params, files=files)
    response.raise_for_status()

# Adding record to RDM
payload = {
    "_at"  : int(round(time.time() * 1000)),
    "_id"  : file_uuid,
    "_rev" : str(uuid.uuid4()),
    "_type": "fs::file",
    "_v"   : 0,
    "name" : file_name,
    "size" : file_size,
    "uuid" : file_uuid
}

if is_valid_uuid(args.folder_uuid):
    payload["parent"] = args.folder_uuid

data_encoded_json = {"data_b64": base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')}
response = session.post(rdm_upload_url, headers=headers, data=json.dumps(data_encoded_json))
response.raise_for_status()
print ("Site {0} file uploaded \n{1}".format(args.siteid, json.dumps(payload, indent=4)))
