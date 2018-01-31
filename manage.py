#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager, Server
from flask_script.commands import ShowUrls
from configs.config import E, APP_NAME

import application

app=application.create_app

manager = Manager(app)
manager.add_option('-c', '--config', dest='config', required=False, choices=E)
manager.add_option('-n', '--name', dest='app_name', required=False, choices=APP_NAME)

manager.add_command("showurls", ShowUrls())

@manager.shell
def make_shell_context():
    """Create a python CLI.
    return: Default import object
    type: `Dict`
    
    """
    from application.extensions import db
    import application.models as Models
    return dict(app=app,
                db=db,
                User=Models.User)


if __name__ == '__main__':
    manager.run()
