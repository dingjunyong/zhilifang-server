# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt


__all__ = ['UserPointRecord']

class UserPointRecord(db.Model):
    '''
    系统用户
    '''
    __tablename__ = 'user_point_records'
    id = db.Column(db.Integer, primary_key=True)
    point = db.Column(db.Integer)
    desc = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __unicode__(self):
        return '%s' % str(self.id)