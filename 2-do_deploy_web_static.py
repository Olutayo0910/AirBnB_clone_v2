#!/usr/bin/python3
"""deployment of archive"""

from fabric.api import *
import os

env.hosts = ["100.26.10.85", "54.158.211.209"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploys archive to two servers"""
    if not os.path.exists(archive_path):
        return False

    results = []

    put_res = put(archive_path, "/tmp")
    results.append(put_res.succeeded)

    base_name = os.path.basename(archive_path)
    if base_name[-4:] == ".tgz":
        name = base_name[:-4]
    newdir = "/data/web_static/releases/" + name
    run("mkdir -p " + newdir)
    run("tar -xzf /tmp/" + base_name + " -C " + newdir)

    run("rm /tmp/" + base_name)
    run("rsync -a {}/web_static/ {}/".format(newdir, newdir))
    run("rm -rf " + newdir + "/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s " + newdir + " /data/web_static/current")

    return True
