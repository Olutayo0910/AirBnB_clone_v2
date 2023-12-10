#!/usr/bin/python3
""" Lets keep it clean"""

from fabric.api import *
import os
from datetime import datetime
import tarfile

env.hosts = ["100.26.10.85", "54.158.211.209"]
env.user = "ubuntu"


def do_clean(number=0):
    """ keep only the most recent version of your archive"""
    number = int(number)
    if number < 2:
        number = 1
    number += 1
    number = str(number)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              number + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
