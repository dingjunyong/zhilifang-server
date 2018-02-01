# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt
from flask_login import UserMixin


__all__ = ['SystemUser']

class SystemUser(db.Model,UserMixin):
    '''
    系统用户
    '''
    __tablename__ = 'system_users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    #date
    create_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    #delete
    is_deleted = db.Column(db.Boolean,default=False)
    deleted_time = db.Column(db.DateTime)

    def __unicode__(self):
        return '%s' % str(self.id)

    def generate_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        print(self._password)

    def check_password(self, password):
        if self.password is None:
            return False
        return bcrypt.check_password_hash(self.password, password)

    @classmethod
    def authenticate(cls, email=None, password=None):
        if email:
            user = cls.query.filter_by(email=email).first()
        else:
            user = None
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated

    def mark_deleted(self):
        if self.is_deleted:
            return
        self.is_deleted = True
        self.deleted_date = datetime.datetime.utcnow()
        db.session.commit()