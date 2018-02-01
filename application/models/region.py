# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt

__all__ = ['Region']

class Region(db.Model):
    '''
    系统用户
    '''
    __tablename__ = 'region'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    type = db.Column(db.Integer)
    agency_id = db.Column(db.Integer)

    def __unicode__(self):
        return '%s' % str(self.id)
