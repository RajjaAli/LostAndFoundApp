import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY = "super secret key"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/posts'



app_config = {
    'development': Development,

}