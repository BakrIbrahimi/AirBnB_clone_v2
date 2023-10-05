#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """A script that generates a .tgz archive from the contents
    of the web_static folder"""
    now = datetime.now()
    time_str = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(time_str)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_name))
        return (archive_name)
    except Exception:
        return None