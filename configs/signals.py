# -*- coding: utf-8 -*-

from blinker import Namespace

_signals = Namespace()


noti = _signals.signal('noti')

# user actions
user_signup = _signals.signal('user_signup')

