#!/usr/bin/python3
"""
    Script that deletes out-of-date archives,
    using the function do_clean
"""
from fabric.api import *

env.hosts = ['34.75.248.214', '35.229.37.122']


def do_clean(number=0):
    """
        Deletes out-of-date archives

        Args:
            number: Number of the archives.
    """
    number = int(number)

    if number in (0, 1):
        number = 1

    number += 1

    local("rm $(ls -d $PWD/versions/* -1t | tail -n +{})".format(number))
