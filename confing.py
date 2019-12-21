#encoding: utf-8
import os
DEBUG = True
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = "710977702@qq.com"
# 这里的密码是你在邮箱中的授权码
MAIL_PASSWORD = "fbkhczcdyaulbced"
# 显示发送人的名字
MAIL_DEFAULT_SENDER = '710977702<710977702@qq.com>'
SECREY_KEY = os.urandom(24)