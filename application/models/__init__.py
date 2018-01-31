# -*- coding: utf-8 -*-
from .user import *
from .permission import *
from .common import *
from .shop import *

def all():
    result = []
    models = [user, permission]
    for m in models:
        result += m.__all__
    return result


__all__ = all()
