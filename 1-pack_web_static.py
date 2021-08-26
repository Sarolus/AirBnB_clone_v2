#!/usr/bin/python3
"""
    Fabric Script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
        Packs the contents of web_static folder
        in a .tgz archive using Fabric.
    """
    try:
        currentDatetime = datetime.now().strftime("%Y%m%d%H%M%S")
        archive = "versions/web_static_{}.tgz".format(currentDatetime)
        local("mkdir -p versions")
        local("tar -vzcf {} web_static".format(archive))
    except Exception:
        return None
