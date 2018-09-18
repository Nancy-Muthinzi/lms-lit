from app import create_app

# script import manger
from flask_script import Manager, Server


app = create_app('development')

# difining a manager to app
manager = Manager(app)


manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()
from app import create_app
from flask_script import Manager, Server


#creating an app instance
app = create_app('development')
# app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app)    

if __name__ == '__main__':
    manager.run()
    
