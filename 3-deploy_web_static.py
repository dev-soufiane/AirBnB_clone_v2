#!/usr/bin/python3
"""
do_pack(): Generates a .tgz archive from the contents of the web_static folder
do_deploy(): Distributes an archive to a web server
deploy (): Creates and distributes an archive to a web server
"""

from fabric.operations import local as fabric_local, run, put
from datetime import datetime as dt
import os
from fabric.api import env as fabric_env
import re

fabric_env.hosts = ['100.26.151.146', '100.25.146.124']

def do_pack():
    """Compresses files into an archive."""
    fabric_local("mkdir -p versions")
    filename = "versions/web_static_{}.tgz".format(dt.strftime(
                                                   dt.now(),
                                                   "%Y%m%d%H%M%S"))
    result = fabric_local("tar -cvzf {} web_static"
                          .format(filename))
    if result.failed:
        return None
    return filename

def do_deploy(archive_path):
    """Distributes an archive to a server."""
    if not os.path.exists(archive_path):
        return False
    rex = r'^versions/(\S+).tgz'
    match = re.search(rex, archive_path)
    filename = match.group(1)
    res = put(archive_path, "/tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    if res.failed:
        return False
    res = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm /tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/releases/{}/web_static"
              .format(filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/current")
    if res.failed:
        return False
    res = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(filename))
    if res.failed:
        return False
    print('New version deployed!')
    return True

def deploy():
    """Creates and distributes an archive to a web server."""
    filepath = do_pack()
    if filepath is None:
        return False
    deploy_result = do_deploy(filepath)
    return deploy_result
