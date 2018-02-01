# -*- coding: utf-8 -*-

from flask_admin.babel import gettext
from flask_admin.contrib.sqla.filters import BaseSQLAFilter
from application.extensions import admin,db
import application.models as Models
from . import MBModelView


class UserView(MBModelView):
    column_list = ('id', 'mobile_number', 'activation_key', 'activate_key_expire_date')
    # form_subdocuments = {
    #     'account': {
    #         'form_columns': ('mobile_number', 'activation_key', 'activate_key_expire_date')
    #     },
    # }

# class LogView(MBModelView):
#     can_create = False
#     column_default_sort = ('created_at', True)
#     column_filters = ('log_type', )
#


# #-----角色-----#
# admin.add_view(MBModelView(Models.Role, db.session,name='角色管理'))
#-----用户-----#
admin.add_view(UserView(Models.User,db.session,name='所有用户',category='用户管理'))
# admin.add_view(MBModelView(Models.SocialOAuth, category='User'))
# admin.add_view(MBModelView(Models.Cart, category='User', endpoint='cartmodel'))
# admin.add_view(MBModelView(Models.EntrySpec, category='User'))
# admin.add_view(MBModelView(Models.Coupon, category='User'))
# admin.add_view(MBModelView(Models.CouponWallet, category='User'))
# admin.add_view(MBModelView(Models.OrderEntry, category='User'))
# admin.add_view(MBModelView(Models.CoinWallet, category='User'))
# admin.add_view(MBModelView(Models.CoinTrade, category='User'))
# admin.add_view(MBModelView(Models.Address, category='User', endpoint='addressmodel'))
# admin.add_view(MBModelView(Models.GuestRecord, category='User'))

