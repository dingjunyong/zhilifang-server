# -*- coding: utf-8 -*-

from . import admin, frontend,website


default_blueprints = [
    frontend.frontend,
]

default_blueprints.extend(website.blueprints)
