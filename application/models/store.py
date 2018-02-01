# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt


__all__ = ['Store']

class Store(db.Model):
    '''
    门店
    '''
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    avatar = db.Column(db.String(255))
    desc = db.Column(db.String(255))
    worktime_desc = db.Column(db.String(255))
    mobile1 = db.Column(db.String(100))
    mobile2 = db.Column(db.String(100))
    country_id= db.Column(db.Integer,default=1)
    province_id = db.Column(db.Integer)
    city_id = db.Column(db.Integer)
    district_id = db.Column(db.Integer)
    address=db.Column(db.String(500))
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