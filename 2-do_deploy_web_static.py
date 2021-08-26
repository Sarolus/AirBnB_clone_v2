#!/usr/bin/python3
"""
    Fabric Script that distributes an archive to your web servers,
    using the function do_deploy
"""
from datetime import datetime
from fabric.api import local, put, run, env
from os import path

env.hosts = ['34.75.248.214', '35.229.37.122']


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
        archive = archive_path.split("/")[-1]
        filename = archive.split(".")[0]
        releases_path = "/data/web_static/releases"

        try:
            put(archive_path, "/tmp/{}".format(archive))

            run("mkdir -p {}/{}/".format(releases_path, filename))
            run("tar -xzf /tmp/{} -C {}/{}/".format(
                archive,
                releases_path,
                filename
            ))

            run("rm /tmp/{}".format(archive))
            run("mv {}/{}/web_static/* {}/{}/".format(
                releases_path,
                filename,
                releases_path,
                filename
            ))

            run("rm -rf {}/{}/web_static".format(
                releases_path,
                filename
            ))
            run("rm -rf /data/web_static/current")

            run("ln -s {}/{}/ /data/web_static/current".format(
                releases_path,
                filename
            ))
            print("New version deployed!")
            return True
        except Exception:
            return False

    except FileNotFoundError:
        return False
