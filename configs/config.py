# -*- coding: utf-8 -*-
import os
import datetime
from .enum import Enum


_basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TEMPLATE_DIR = os.path.join(_basedir,'application', 'templates')


E = Enum(['development', 'production', 'test'])
APP_NAME = Enum(['webapp', 'worker', 'admin'])


class BaseConfig(object):
    PROJECT = APP_NAME.webapp
    VERSION = '2018.1.20'
    DEBUG = True
    TESTING = False
    PROD = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}


    # Flask Toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_PANELS = [
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel'
    ]

    ENV = E.development

    ADMINS = frozenset(['season@maybi.cn'])

    # os.urandom(24)
    SECRET_KEY = 'WhatIsTheMeaningOfLife'
    IDCARD_KEY = 'HowAreYouDoing'
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False

    UPLOAD_FOLDER = os.path.join(_basedir, 'application', 'static/csv/')

    AVATAR_FOLDER = os.path.join(_basedir, 'application/static/img/avatar')

    # ===========================================
    # Maybi
    #
    # flask session, should available for all sub domain
    # SESSION_COOKIE_DOMAIN = '.maybi.cn'
    # SERVER_NAME = 'maybi.cn'

    # Flask-login
    REMEMBER_COOKIE_DOMAIN = '.maybi.cn'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=31)

    # ===========================================
    # Flask-cache
    CACHE_TYPE = 'null'

    TRACKING_EXCLUDE = (
        '^/favicon.ico',
        '^/static/',
        '^/admin/',
        '^/_debug_toolbar/',
    )



class ProdConfig(BaseConfig):
    DEBUG = True
    PROD = True
    ENV = E.production
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@127.0.0.1:3306/zlf_car'


class DevConfig(BaseConfig):
    DEBUG = True
    ENV = E.development
    # ===========================================
    # Flask-Assets
    #
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@127.0.0.1:3306/zlf_car'


class TestConfig(DevConfig):
    TESTING = True
    ENV = E.test
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@127.0.0.1:3306/zlf_car'
    # flask cache
    CACHE_TYPE = 'null'
    CACHE_NO_NULL_WARNING = True

config_map = {
    'development': DevConfig,
    'test': TestConfig,
    'production': ProdConfig,
}


def get_config(env, app=''):
    if app == 'worker':
        env = 'production'
    return config_map[env]()

def get_config_from_host(app_name):
    flask_env = os.environ.get('FLASK_ENV','production')
    config = get_config(flask_env, app_name)
    return config
