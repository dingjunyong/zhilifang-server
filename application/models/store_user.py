# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt


__all__ = ['StoreUser']

class StoreUser(db.Model):
    '''
    系统用户
    '''
    __tablename__ = 'store_users'
    id = db.Column(db.Integer, primary_key=True)
    mobile = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))
    store_id = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, default=db.func.current_timestamp())
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