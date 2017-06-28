"""
This file contains the configuration variables for the app
http://flask.pocoo.org/docs/0.12/config/
"""

class Config(object):
    """
    Common configurations
    Put any configurations here that are common across all environments
    """
    import os
    BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 
   
    CSRF_ENABLED = True                                  # Enable protection agains *Cross-site Request Forgery (CSRF)*

    # Flask-Login Settings
    REMEMBER_COOKIE_SECURE = True

    #BCRYPT Settings

    #BCRYPT_LOG_ROUNDS=12  #This value is used in determining the complexity of the encryption
    #BCRYPT_HASHPREFIX=
    #BCRYPT_HANDLE_LONG_PASSWORDS=


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    #Flask Settings
    DEBUG = True
    
    SQLALCHEMY_ECHO = True

    BCRYPT_LOG_ROUNDS = 12


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}