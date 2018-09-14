import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import click
import config

from app import create_app

app = create_app('development')

@app.cli.command('urlmap')
def urlmap():
    echo("{:50s} {:40s} {}".format('Endpoint', 'Methods', 'Route'))
    for route in app.url_map.iter_rules():
        methods = ','.join(route.methods)
        echo("{:50s} {:40s} {}".format(route.endpoint, methods,route))

@app.cli.command('ipython')
def ipython():
    try:
        import IPython
    except ImportError:
        echo("IPython not found, make sure you run pip install -r requirements.txt")
        return
    from flask.globals import _app_ctx_stack
    app = _app_ctx_stack.top.app
    banner = 'Python %s on %s\nIPython: %s\nApp: %s%s\nInstance: %s\n' % (
        sys.version,
        sys.platform,
        IPython.__version__,
        app.import_name,
        app.debug and ' [debug]' or '',
        app.instance_path,
    )

    ctx = {}

    startup = os.environ.get('PYTHONSTARTUP')
    if startup and os.path.isfile(startup):
        with open(startup, 'r') as f:
            eval(compile(f.read(), startup, 'exec'), ctx)

    ctx.update(app.make_shell_context())

    IPython.embed(banner1=banner, user_ns=ctx)
        
app.config.from_object(os.environ['APP_SETTINGS'])
#
#migrate = Migrate(app, db)
manager = Manager(app)
#
#manager.add_command('db', MigrateCommand)
#
#
if __name__ == '__main__':
    manager.run()
