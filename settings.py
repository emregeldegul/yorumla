from os import path, urandom

BASEDIR = path.abspath(path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASEDIR, 'demongo.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "demongo"
ADMINS = ["admin@yorumla.com"]
MAIL_SERVER = "smtp.elasticemail.com"
MAIL_USERNAME = "baxixi4141@dghetian.com"
MAIL_PASSWORD = '3C7CBAC4E211DCFE88583FF6A55E8DBD3232'
MAIL_PORT = 2525
MAIL_USE_SSL = True
MAIL_USE_TLS = False
