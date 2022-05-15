from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Blog
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)