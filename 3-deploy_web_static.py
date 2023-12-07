#!/usr/bin/python3
"""Full deployment script"""

from fabric.api import local, env, run, put
from datetime import datetime
import os
env.hosts = ["100.26.10.85", "54.158.211.209"]
env.user = "ubuntu"


def do_pack():
    """Create a compressed archive of web_static"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)

        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        print("Error creating archive:", str(e))
        return None


def do_deploy(archive_path):
    """Deploy the archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        base_name = os.path.basename(archive_path)
        name = base_name.split('.')[0]
        newdir = "/data/web_static/releases/" + name

        put_res = put(archive_path, "/tmp")
        if not put_res.succeeded:
            return False

        run("mkdir -p {}".format(newdir))
        run("tar -xzf /tmp/{} -C {}".format(base_name, newdir))
        run("rm /tmp/{}".format(base_name))
        run("rsync -a {}/web_static/ {}/".format(newdir, newdir))
        run("rm -rf {}/web_static".format(newdir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(newdir))

        return True
    except Exception as e:
        print("Error deploying archive:", str(e))
        return False


def deploy():
    """Deploy the web_static content"""
    archive_path = do_pack()

    if archive_path:
        return do_deploy(archive_path)
    else:
        return False


if __name__ == "__main__":
    deploy()
