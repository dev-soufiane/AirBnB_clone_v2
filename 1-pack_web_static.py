#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder.
"""

from fabric.operations import local as fabric_local
from datetime import datetime as dt

def do_pack():
    """Function to compress files"""
    fabric_local("mkdir -p versions")
    result = fabric_local("tar -cvzf versions/web_static_{}.tgz web_static"
                          .format(dt.strftime(dt.now(), "%Y%m%d%H%M%S")),
                          capture=True)
    if result.failed:
        return None
    return result
