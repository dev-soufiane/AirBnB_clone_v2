#!/usr/bin/python3
from fabric.api import local as fabric_local
from time import strftime as fmt_time
from datetime import date as dt

def do_pack():
    """Generates and archives the contents of the web_static folder."""

    timestamp = fmt_time("%Y%m%d%H%M%S")
    try:
        fabric_local("mkdir -p versions")
        fabric_local("tar -czvf versions/web_static_{}.tgz web_static/"
                     .format(timestamp))

        return "versions/web_static_{}.tgz".format(timestamp)

    except Exception as e:
        return None
