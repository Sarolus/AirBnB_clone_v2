#!/usr/bin/python3
"""
    Fabric Script that distributes an archive to your web servers,
    using the function do_deploy
"""
from datetime import datetime
from fabric.api import local, put, run, env
from os import path

env.hosts = ['34.75.248.214', '35.229.37.122']
env.key_identity_file = "~/.ssh/holberton"
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """
        Deploy the given archive to the web_server

        Args:
            archive_path: path of the archive to deploy.
    """
    try:
        filename = archive_path.split("/")[-1]
        filename_no_ext = path.splitext(filename)
        remote_data = "/data/web_static/releases"

        try:
            put(archive_path, "/tmp/")

            run("mkdir -p {}/{}/".format(remote_data, filename_no_ext))
            run("tar -xzf /tmp/{} -C {}/{}/".format(
                filename,
                remote_data,
                filename_no_ext
            ))

            run("rm -f /tmp/{}".format(filename))
            run("mv {}/{}/web_static/* {}/{}/".format(
                remote_data,
                filename_no_ext,
                remote_data,
                filename_no_ext
            ))

            run("rm -rf {}/{}/web_static".format(remote_data, filename_no_ext))
            run("rm -rf /data/web_static/current")

            run("ln -s {}/{}/ /data/web_static/current".format(
                remote_data,
                filename_no_ext
            ))
            return True
        except Exception:
            return False

    except FileNotFoundError:
        return False
