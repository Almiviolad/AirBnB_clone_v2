#!/usr/bin/python3
""" A fabric script that generates a .tgz archive"""
from fabric.api import local
import time
def do_pack():
    """Gets an tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        final = local("tar -cvzf versions/web_static_{}.tgz web_static/".format(time.strftime("%Y%m%d%H%M%S")))
        return final
    except:
        return None
