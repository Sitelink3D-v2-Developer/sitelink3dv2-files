#!/usr/bin/python
import argparse
import logging
import os
import sys
import requests
from tqdm import tqdm

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
arg_parser = argparse.ArgumentParser(description="File Download")

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
arg_parser.add_argument("--file-uuid", help="File uuid")

arg_parser.set_defaults()
args = arg_parser.parse_args()
logging.basicConfig(format=args.log_format, level=args.log_level)
# << Arguments


# << Server settings
scheme, host, port = shp(args.env, SR_EDGE_SCHEME, SR_EDGE_HOST, SR_EDGE_PORT)
server_url = "{}://{}-{}:{}".format(scheme, args.dc, host, port)
get_file_url = "{0}/file/v1/sites/{1}/files/{2}/url".format(server_url, args.siteid, args.file_uuid)
oauth_edge_url = "{0}/oauth/v1/token".format(server_url)
headers = {'content-type': 'application/json', 'X-Topcon-Auth': args.jwt}
session = requests.Session()
if args.env == "local":
    session.verify = False
if len(args.oauth_id) > 0 and len(args.oauth_secret) > 0 and len(args.oauth_scope) > 0:
    # get oauth token
    headers = get_oauth_header(oauth_edge_url, args.oauth_id, args.oauth_secret, args.oauth_scope)
# << Server settings

# get the url of the file
response = session.get(get_file_url, headers=headers)
response.raise_for_status()

# get the content of the url
url = "{0}{1}".format(server_url, response.text)
print ("get file {0} by url {1}".format(args.file_uuid, url))
response = session.get(url, headers=headers, stream=True)
response.raise_for_status()
with open('./{0}'.format(args.file_uuid), "wb") as handle:
    for data in tqdm(response.iter_content()):
        handle.write(data)
