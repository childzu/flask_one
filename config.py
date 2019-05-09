# config.py

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    print('System running in mode : Development')
    DEBUG = True
    SQLALCHEMY_ECHO = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    print('System running in mode : Production')

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}