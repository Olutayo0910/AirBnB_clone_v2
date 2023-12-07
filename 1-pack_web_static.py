#!/usr/bin/python3
"""Fabric script that generates a .tgz"""
import tarfile
import os
from datetime import datetime



def do_pack():
    """creates .tgz file"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{date}.tgz"
    if not os.path.exists("versions/"):
        os.mkdir("versions/")
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(archive_name):
        return archive_name
    else:
        return None
