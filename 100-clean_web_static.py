#!/usr/bin/python3
"""This module contains a fabric script that
removes old web versions"""
from fabric.api import env, lcd, local, run
env.hosts = ['35.243.194.38', '54.91.79.148']


def do_clean(number=0):
    """This function removes unnecesary old versions"""
    n = int(number)
    if n < 0:
        return

    n = n + 1 if n > 0 else 2
    cmd = 'rm -rf $(ls -1t | tail -n+{})'.format(n)

    with lcd('versions'):
        local(cmd)

    with lcd('/data/web_static/releases'):
        run(cmd)
