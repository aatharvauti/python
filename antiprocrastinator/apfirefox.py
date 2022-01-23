import json
import lz4.block
import os
import signal

# set home (tested on Linux and Mac, I don't have windows :)
# this returns /home/username
home = os.path.expanduser('~/')

# open the "recovery.jsonlz4" located in sessionstore-backups
# r: read, b: binary mode
file = open(f"{home}/.mozilla/firefox/tt5rz730.default-release/sessionstore-backups/recovery.jsonlz4", "rb")
# read(8) where 8 are no. of bytes
file.read(8)

# load and decompress the lz4 compressed block, and decode it to utf8
data = json.loads(lz4.block.decompress(file.read()).decode("utf-8"))
file.close()

# session refers to current tab in firefox
session = ""

# sorting out json data to get the url of current tab
for win in data.get("windows"):
    for tab in win.get("tabs"):
        i = int(tab.get("index")) - 1
        session = tab.get("entries")[i].get("url")