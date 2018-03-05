#!/usr/bin/env python

import winrm
import re
import click


@click.command()
@click.option('-h', '--hostname', 'hostname', required=True)
@click.option('-u', '--username', 'username', required=True)
@click.option('-p', '--password', 'password', required=True)
@click.option('-c', '--command', 'command', required=True)


def execute_winrm(hostname, username, password, command):
    s = winrm.Session(hostname, auth=(username, password))
    r = s.run_ps(command)
    print(re.sub(rb'\r\n', b'\n', r.std_out).decode('utf-8'))

if __name__ == '__main__':
    execute_winrm()
