# -*- coding: utf-8 -*-

import os
from redis import ConnectionPool
from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, request, jsonify, g, session, current_app, redirect
from flask_principal import PermissionDenied, identity_loaded
from application.extensions import (db,cache, admin, login_manager,
    principal, bcrypt, toolbar, assets,
    redis, session_redis
)
import configs.config as ConfigsModel
from application.redis_session_interface import RedisSessionInterface
from application.services.permission import principal_on_identity_loaded
import application.models as Models

# For import *
__all__ = ['create_app']


def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = ConfigsModel.BaseConfig.PROJECT

    if app_name != ConfigsModel.APP_NAME.worker:
        import application.controllers as Controllers

    app = Flask(app_name,
                static_folder='application/static',
                template_folder='application/templates')

    configure_app(app, config)
    configure_hook(app, app_name)
    configure_extensions(app)
    configure_blueprints(app, app_name, blueprints)
    configure_logging(app)
    configure_template_filters(app)
    configure_error_handlers(app)
    if app_name != ConfigsModel.APP_NAME.worker:
        configure_admin(app)
    #app.wsgi_app = ProxyFix(app.wsgi_app)
    # _password = bcrypt.generate_password_hash("admin").decode('utf-8')
    # print(_password)
    return app


def configure_app(app, config):
    """
    Configure app from object, parameter and env.
    @config the config of application
        - is either an string ['test','production','staging', 'development']
        - or an configuration object
    """
    BaseConfig = ConfigsModel.BaseConfig

    config = ConfigsModel.get_config_from_host(app.name)
    app.config.from_object(config)

    # Override setting by env var without touching codes.
    app.config.from_envvar(
        '%s_APP_CONFIG' % BaseConfig.PROJECT.upper(), silent=True)

def configure_extensions(app):
    """
    注册扩展
    :param app: 
    :return: 
    """
    # --- DB --- #
    db.init_app(app)

    # redis.connection_pool = ConnectionPool(**app.config.get('REDIS_CONFIG'))
    # session_redis.connection_pool = ConnectionPool(
    #     **app.config.get('SESSION_REDIS'))
    #
    # # server side session
    # app.session_interface = RedisSessionInterface(session_redis)

    # flask-cache
    cache.init_app(app)

    # flask-bcrypt
    bcrypt.init_app(app)

    # flask-assets
    assets.init_app(app)

    # flask_debugtoolbar
    toolbar.init_app(app)

    # flask-login (not configured will raise 401 error)
    login_manager.login_view = 'frontend.login'

    # login_manager.refresh_view = 'frontend.reauth'

    @login_manager.user_loader
    def load_user(id):
        user= Models.User.query.filter_by(id=id, is_deleted=False).first()
        return user

    login_manager.init_app(app)
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.needs_refresh_message = 'Please reauthenticate to access this page.'

    # flask-principal (must be configed after flask-login!!!)
    principal.init_app(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        principal_on_identity_loaded(sender, identity)



def configure_blueprints(app,app_name,blueprints):
    """Configure blueprints in views."""
    if app_name == ConfigsModel.APP_NAME.worker:
        return
    import application.controllers as Controllers
    if app_name == ConfigsModel.APP_NAME.webapp:
        blueprints = Controllers.default_blueprints

    elif app_name == ConfigsModel.APP_NAME.admin:
        blueprints = [Controllers.frontend.frontend]

    else:
        blueprints = Controllers.default_blueprints

    if blueprints:
        for blueprint in blueprints:
            app.register_blueprint(blueprint)

def configure_template_filters(app):
    pass

def configure_logging(app):
    """Configure file(info) and email(error) logging."""

    if app.debug or app.testing:
        # Skip debug and test mode.
        # You can check stdout logging.
        return

    import logging
    from logging.handlers import SMTPHandler

    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.INFO)

    info_log = os.path.join(app.root_path, "..", "logs", "app-info.log")
    info_file_handler = logging.handlers.RotatingFileHandler(
        info_log, maxBytes=1048576, backupCount=20)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)

    ADMINS = ['seasonstar@126.com']
    mail_handler = SMTPHandler(app.config['MAIL_SERVER'],
                               app.config['MAIL_USERNAME'],
                               ADMINS,
                               'O_ops... %s failed!' % app.config['PROJECT'],
                               (app.config['MAIL_USERNAME'],
                                app.config['MAIL_PASSWORD']))
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(mail_handler)

def configure_hook(app,app_name):

    @app.before_request
    def before_request():
        pass

def configure_error_handlers(app):
    @app.errorhandler(PermissionDenied)
    def permission_error(error):
        ''' permission denied exception from flask principal'''
        return jsonify(
            message='Failed', code=403, error='Permission Denied')

    @app.errorhandler(401)
    def login_required_page(error):
        ''' exception thrown out by flask login'''
        return jsonify(message='Failed', code=401, error='Login required')

    @app.errorhandler(403)
    def forbidden_page(error):
        return jsonify(
            message='Failed', code=403, error='Permission Denied')

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify(message='Failed', code=404, error='Page not found')

    @app.errorhandler(500)
    def server_error_page(error):
        return jsonify(
            message='Failed', code=500, error='Internal Server error')

def configure_admin(app):
    from application.controllers.admin.dashboard import IndexView
    admin.name = u"汽车服务管理平台"
    admin.base_template = 'admin/master2.html'
    admin.template_mode = 'bootstrap3'
    admin.init_app(app)
    admin.index_view = IndexView(name="Dashboard")

