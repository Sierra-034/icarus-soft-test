
class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/icarus_soft'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/icarus_soft_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_dict = {
    'test': TestingConfig,
    'development': DevelopmentConfig,
}
