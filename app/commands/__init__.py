# -*- coding: utf-8 -*-
import urllib

from flask import current_app

from app import script_manager

script_manager.add_default_commands()


@script_manager.command
def list_routes():
    output = []
    for rule in current_app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print line
