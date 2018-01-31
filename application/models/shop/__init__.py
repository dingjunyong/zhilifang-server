# -*- coding: utf-8 -*-

from .shop import *

def all():
    result = []
    models = [shop]
    for m in models:
        result += m.__all__
    return result


__all__ = all()
