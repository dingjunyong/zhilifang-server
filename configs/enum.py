# -*- coding: utf-8 -*-

class Enum(list):
    ''' Enumeration class '''
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

    def __add__(self, other):
        # list addition
        result = super(Enum, self).__add__(other)
        return Enum(result)


class TupleEnum(list):
    '''
     Enumeration class expecting element as 2-tuple
    '''
    def __getattr__(self, name):
        keys = [k for k, v in self]
        if name in keys:
            return name
        raise AttributeError

    def __add__(self, other):
        # list addition
        result = super(TupleEnum, self).__add__(other)
        return TupleEnum(result)

    def __contains__(self, key):
        keys = [k for k, v in self]
        return key in keys


class DictEnum(dict):
    __getattr__ = lambda self, k: DictEnum(self.get(k)) if type(self.get(k)) is dict else self.get(k)



#---用户类枚举---#
USER_ROLE = Enum(['ADMIN',
                  'SHOP_OWNER',
                  'SHOP_SELLER',
                  'MEMBER'])

USER_STATUS = Enum(['ACTIVE', 'INACTIVE', 'NEW'])

USER_GENDER = Enum(['M', 'F'])

#---通知枚举---#
NOTI_TYPE = Enum([
    'USER_SIGNUP',  # noti after user signup
] )

