# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt

__all__ = ['Card']

class Card(db.Model):
    '''
    系统用户
    '''
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(500))
    price  = db.Column(db.Integer,default=199)

    def __unicode__(self):
        return '%s' % str(self.id)
