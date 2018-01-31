# -*- coding: utf-8 -*-

SOCIALOAUTH_SITES = (
    ('wechat', 'socialoauth.sites.wechat.Wechat', '微信',
        {
          'redirect_uri': 'http://m.maybi.cn/account/oauth/wechat',
          'client_id': '',
          'client_secret': '',
          'scope': 'snsapi_userinfo'
        }
    ),
    ('wechat_app', 'socialoauth.sites.wechat_app.WechatApp', '微信客户端',
        {
          'redirect_uri': 'http://m.maybi.cn/account/oauth/wechat',
          'client_id': '',
          'client_secret': '',
          'scope': 'snsapi_userinfo'
        }
    ),
)