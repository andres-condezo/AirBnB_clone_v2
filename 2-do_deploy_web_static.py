#!/usr/bin/python3
"""This module contains a fabric script that
creates and distributes an archive to the web servers"""
from fabric.api import env, put, run
from datetime import datetime as dt
from os import path

env.hosts = ['35.243.194.38', '54.91.79.148']
path_releases = '/data/web_static/releases'


def do_deploy(archive_path):
    """This function distributs an archive file"""
    if not path.isfile(archive_path):
        return False
    filename = archive_path.split('/')[-1]
    fname = filename.split('.')[0]
    if put(archive_path, '/tmp/{}'.format(filename)).failed:
        return False
    if run('mkdir -p /data/web_static/releases/{}'
            .format(fname)).failed:
        return False
    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
            .format(filename, fname)).failed:
        return False
    if run('rm /tmp/{}'.format(filename)).failed:
        return False
    path_web = '{}/{}'.format(path_releases, fname)
    if run('mv {}/web_static/* {}'
            .format(path_web, path_web)).failed:
        return False
    if run('rm -rf {}/web_static'.format(path_web)).failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run('ln -s {} /data/web_static/current'.
            format(path_web)).failed:
        return False
    return True
