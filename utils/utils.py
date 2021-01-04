#!/usr/bin/python
import base64
import requests
import uuid

# >> Server URL:
def shp(env, s,h,p):
    if env is None:    return s,h,p
    if env == "local": return "https", "api.edge-router", "443"
    if env == "qa":    return "https", "qa-api.code.topcon.com", "443"
    if env == "prod":  return "https", "api.code.topcon.com", "443"
    raise ValueError("no idea about env={}".format(env))

# Get OAuth header
def get_oauth_header(oauth_edge_url, oauth_id, oauth_secret, oauth_scope):
    # https://tools.ietf.org/html/rfc6749#section-4.4
    headers = {"Authorization": "Basic " + base64.b64encode(("{0}:{1}".format(oauth_id, oauth_secret)).encode('utf-8')).decode('utf-8')}
    params = {"grant_type": "client_credentials"}
    scopes = oauth_scope.split()
    if len(scopes) > 0:
        params["scope"] = scopes
    session = requests.Session()
    if "edge-router" in oauth_edge_url:
        session.verify = False
    r = session.post(oauth_edge_url, params=params, headers=headers)
    r.raise_for_status()
    jwt = r.json()['access_token']
    return {"Authorization": "Bearer " + jwt, "content-type": "application/json"}

# Validate UUID
def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False
