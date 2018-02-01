# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt


__all__ = ['UserCard']

class UserCard(db.Model):
    '''
    系统用户
    '''
    __tablename__ = 'user_cards'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    card_id = db.Column(db.Integer)
    number = db.Column(db.String(100))
    desc = db.Column(db.String(500))
    start_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    end_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_deleted = db.Column(db.Boolean, default=False)
    deleted_time = db.Column(db.DateTime)

    def __unicode__(self):
        return '%s' % str(self.id)


