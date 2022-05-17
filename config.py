import os

class Config:
    '''
    General configuration parent class
    '''
    

# email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY='1234m'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QOUTES_API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_TRACK_MODIFICATIONS="False"
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://maureen:1234@localhost/chicblog'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maureen:1234@localhost/chicblog'
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = uri
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://maureen:1234@localhost/chicblog'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://maureen:1234@localhost/chicblog'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}