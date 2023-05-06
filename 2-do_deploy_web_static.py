#!/usr/bin/python3
"""distributes archives to web servers"""

from datetime import datetime
from fabric.api import *
import os.path

env.hosts = ['54.173.84.235', '34.207.155.43']


def do_deploy(archive_path):
    """ distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\releases/web_static_{}/'
            .format(timestamp))
        # uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
        /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))
        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
        /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))
        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
            .format(timestamp))

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run('sudo ln -s /data/web_static/releases/\
        web_static_{}/ /data/web_static/current'.format(timestamp))
        return True
    except Exception as e:
        return False
