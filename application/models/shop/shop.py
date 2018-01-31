# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt
from flask_login import UserMixin

from configs.enum import USER_ROLE
from configs import signals

__all__ = ['Shop']



users_roles = db.Table('users_shops',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('shop_id', db.Integer, db.ForeignKey('shops.id')),
    db.Column('is_manager', db.Boolean, default=False))


class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    img = db.Column(db.String(255))
    telephone1 = db.Column(db.String(100))
    telephone2 = db.Column(db.String(100))
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(255))
    free_times = db.Column(db.Integer, default=2)
    use_description = db.Column(db.String(100), default=2)
    shop_description = db.Column(db.Text)
    statu = db.Column(db.Integer, default=0)
    is_deleted = db.Column(db.Boolean,default=False)
    deleted_date = db.Column(db.DateTime)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    @classmethod
    def create(cls, name):
        shop = Shop(name=name)
        db.session.add(shop)
        db.session.commit()
        return shop

    @classmethod
    def mark_deleted(cls):
        if cls.is_deleted:
            return
        cls.is_deleted = True
        cls.deleted_date = datetime.datetime.utcnow()
        db.session.commit()