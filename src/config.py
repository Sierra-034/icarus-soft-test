
class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/icarus_soft_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_dict = {
    'development': DevelopmentConfig,
}
