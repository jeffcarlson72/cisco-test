#!/usr/bin/env python3

import json
import os
import sys
import urllib.request

def _help():
    print("Usage:  %s MA:CA:DD:RE:SS:00" % sys.argv[0])
    print("You need to put your API key in ~/.macaddress.io.key")
    print("This file must not be readable or writable by others")
    print("(chmod 0600 ~/.macaddress.io.key)")
    exit(0)

if len(sys.argv) != 2: _help()

key_file = os.environ['HOME'] + "/.macaddress.io.key"
if os.path.isfile(key_file):
    if os.stat(key_file).st_mode & 0o777 > 0o700: _help()
    with open(key_file) as k:
        api_key = k.read().rstrip()
else:
    _help()

url = 'https://api.macaddress.io/v1?apiKey=' + \
    api_key + \
    '&output=json&search=' + \
    sys.argv[1]

with urllib.request.urlopen(url) as r:
    j = json.load(r)
    print(j['vendorDetails']['companyName'])
