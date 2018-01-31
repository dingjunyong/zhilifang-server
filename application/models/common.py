# -*- coding: utf-8 -*-
from application.extensions import db
from sqlalchemy.orm import relationship


__all__ = ['City']

class City(db.Model):
    __tablename__ = 'citys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    state =   db.Column(db.String(80))
    statu = db.Column(db.Integer, default=1)


