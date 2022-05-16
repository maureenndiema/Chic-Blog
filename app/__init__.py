from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db=SQLAlchemy()
mail=Mail()
simple = SimpleMDE()
photos = UploadSet('photos', IMAGES)

def create_app(config_name):

    #Initializing the application
    app = Flask(__name__)

    #setting up configurations
    app.config.from_object(config_options[config_name])

    # configure UploadSet
    configure_uploads(app, photos)

    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)


    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Registering thr auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    # setting config
    from .request import configure_request
    configure_request(app)

    return app
