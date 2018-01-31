# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

from flask_cache import Cache
cache = Cache()

from flask_admin import Admin
admin = Admin()

from flask_login import LoginManager
login_manager = LoginManager()

from flask_principal import Principal
principal = Principal()

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# from flask_babel import Babel
# babel = Babel()

from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension()

from flask_assets import Environment
assets = Environment()

from redis import Redis
redis = Redis()
session_redis = Redis()
