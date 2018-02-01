# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt

__all__ = ['StoreActivity','StoreActivityType']

class StoreActivity(db.Model):
    '''
    系统用户
    '''
    __tablename__ = 'store_activities'
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    poster_img = db.Column(db.String(255))
    desc = db.Column(db.Text)
    every_count = db.Column(db.Integer)
    max_count  = db.Column(db.Integer)
    store_id = db.Column(db.String(255))
    is_hot = db.Column(db.Boolean,default=True)
    create_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_deleted = db.Column(db.Boolean,default=False)
    deleted_time = db.Column(db.DateTime)

    def __unicode__(self):
        return '%s' % str(self.id)

    def mark_deleted(self):
        if self.is_deleted:
            return
        self.is_deleted = True
        self.deleted_date = datetime.datetime.utcnow()
        db.session.commit()


class StoreActivityType(db.Model):
    '''
    系统用户
    '''
    __tablename__ = 'store_activity_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __unicode__(self):
        return '%s' % str(self.id)

