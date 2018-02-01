# -*- coding: utf-8 -*-
from .user import *
from .user_card import *
from .user_pointrecord import *
from .region import *
from .store import *
from .store_user import *
from .store_activity import *
from .system_user import *
from .card import *

def all():
    result = []
    models = [user, region, store, store_user , system_user,card]
    for m in models:
        result += m.__all__
    return result


__all__ = all()
