import os

class Config:
    '''
    General configuration parent class
    '''
    pass

# email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = ''
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI =''

class DevConfig(Config):
       '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
SQLALCHEMY_DATABASE_URI =''
DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}