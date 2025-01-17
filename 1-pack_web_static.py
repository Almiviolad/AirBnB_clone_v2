#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
from time import strftime


def do_pack():
    """Create compressed acrvhive of the Airbnb releases"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = 'web_static_{}.tgz'.format(date)
    local('mkdir -p versions')
    local('tar -cvzf versions/{} web_static'.format(filename))
    if local('test -f versions/{}'.format(filename)).succeeded:
        return ("versions/"+filename)
    else:
        return None
