from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean

from <%= appName %>.app import create_app

app = create_app()

manager = Manager(app)
manager.add_command("server", Server(host="0.0.0.0", port=8000))
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """
    return dict(app=app)

if __name__ == '__main__':
    manager.run()
