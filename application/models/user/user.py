# -*- coding: utf-8 -*-
import datetime
from application.extensions import db, bcrypt
from flask_login import UserMixin
from configs.enum import USER_ROLE

__all__ = ['User']


users_roles = db.Table('users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')))


# class UserAccount(db.Model):
#     __tablename__ = 'user_accounts'
#
#     id = db.Column(db.Integer, primary_key=True)
#     # login related
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     email = db.Column(db.String(100))
#     mobile_number = db.Column(db.String(100))
#     is_email_verified = db.Column(db.Boolean,default=False)
#     _password = db.Column(db.String(255))
#     activation_key = db.Column(db.String(255))
#     activate_key_expire_date = db.Column(db.DateTime)
#     created_at = db.Column(db.DateTime, default=db.func.current_timestamp())



    # # ===============================================
    # # password
    # @property
    # def password(self):
    #     return self._password
    #
    # @password.setter
    # def password(self, password):
    #     self._password = bcrypt.generate_password_hash(password).decode('utf-8')
    #     print (self._password)
    #
    # def check_password(self, password):
    #     if self.password is None:
    #         return False
    #     return bcrypt.check_password_hash(self.password, password)
    #
    # def to_json(self):
    #     return dict(created_at=str(self.created_at),
    #                 email=self.email)

class User(db.Model,UserMixin):
    '''
    The UserAccount class contains user personal informations
    and account settings
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    mobile_number = db.Column(db.String(100))
    username = db.Column(db.String(100))
    is_email_verified = db.Column(db.Boolean, default=False)
    _password = db.Column(db.String(255))

    #date
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    #delete
    is_deleted = db.Column(db.Boolean,default=False)
    deleted_at = db.Column(db.DateTime)

    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('users'))

    def __unicode__(self):
        return '%s' % str(self.id)

    # ===============================================
    # password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')
        print(self._password)

    def check_password(self, password):
        if self.password is None:
            return False
        return bcrypt.check_password_hash(self.password, password)

    def to_json(self):
        return dict(created_at=str(self.created_at),
                    email=self.email)

    @property
    def is_admin(self):
        return USER_ROLE.ADMIN in self.roles

    @classmethod
    def is_adminaaa(self):
        aa=self.roles
        print(aa)

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

    # @classmethod
    # def create(cls, email, password, name, mobile_number=None):
    #
    #     account = UserAccount(email=email.lower(),
    #                           mobile_number=mobile_number,
    #                           is_email_verified=True)
    #     account.password = password
    #
    #     db.session.add(account)
    #
    #     user = User(username=name,
    #                 account=account)
    #
    #     db.session.add(account)
    #     db.session.commit()
    #
    #     #signals.user_signup.send('system', user=user)
    #     return user

    def mark_deleted(self):
        if self.is_deleted:
            return
        # delete social oauth, otherwise user can still login via wechat
        # SocialOAuth.objects(user=self).delete()
        self.is_deleted = True
        self.deleted_date = datetime.datetime.utcnow()
        db.session.commit()


