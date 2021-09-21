from app.api.v1.models.user_models import Customer,Restaurant,Pizza
from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server

app = create_app('development')

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db,Customer =Customer, Restaurant = Restaurant, Pizza = Pizza )
if __name__ == '__main__':
    manager.run()