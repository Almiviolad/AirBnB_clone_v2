#!/usr/bin/env python3
"""distributes archives to web servers"""


from fabric.api import *
import os.path

env.hosts = ['54.173.84.235', '34.207.155.43']


def do_deploy(archive_path):
    """ distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        path = archive_path
        file_name = path.split('/')[-1]
        put(path, '/tmp/{}'.format(file_name))
        run('mkdir -p /data/web_static/releases/{}'.format(file_name.split('.')[0]))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_name, file_name.split('.')[0]))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            file_name.split('.')[0]))
        run('rm -rf /data/web_static/current')
        # Create new symbolic link /data/web_static/current
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(file_name.split('.')[0]))
        return True

    except Exception as e:
        return False
