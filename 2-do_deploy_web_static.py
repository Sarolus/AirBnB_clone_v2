#!/usr/bin/python3
"""
    Fabric Script that distributes an archive to your web servers,
    using the function do_deploy
"""
from datetime import datetime
from fabric.api import local, put, run, env
from os import path


def do_deploy(archive_path):
    """
        Deploy the given archive to the web_server

        Args:
            archive_path: path of the archive to deploy.
    """
    try:
        filename = archive_path.split("/")[-1]
        filename_no_ext = filename.splitext(filename)
        remote_data = "/data/web_static/releases"

        try:
            put(archive_path, "/tmp/")

            run("mkdir -p {}{}/".format(remote_data, filename_no_ext))
            run("tar -xzf /tmp/{} -C {}{}/".format(
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

            run("rm -rf {}{}".format(remote_data, filename_no_ext))
            run("rm -rf /data/web_static/current")

            run("ln -sf {}{}/ /data/web_static/current".format(
                remote_data,
                filename_no_ext
            ))
            return True
        except Exception:
            return False

    except FileExistsError:
        return False
