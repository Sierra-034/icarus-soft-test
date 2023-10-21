import os


class DevelopmentConfig:
    DEBUG = False
    DEVELOPMENT = False
    SQLALCHEMY_DATABASE_URI = os.getenv( "SQLALCHEMY_DATABASE_URI", )
