# -*- coding: utf-8 -*-
from application.extensions import db


__all__ = ['Address']


class Address(db.Model):
    '''
    地址管理
    '''
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(255))
    telephone1 =  db.Column(db.String(100))
    telephone2 = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    def __unicode__(self):
        return '%s' % str(self.id)

    @property
    def fields(self):
        return ['state', 'city', 'street', 'telephone1', 'telephone2']

    def to_json(self):
        result = {f: getattr(self, f) for f in self.fields}
        result.update({'id': str(self.id)})
        return result



