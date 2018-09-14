import app

app = create_app()

@app.route('/')
@app.route('/index')
def index():
    if dev == 1:
        hosts = {'localhost', '127.0.0.1'}

    else:
        hosts = {'fmc', 'jumphost'}

    return render_template('index.html', title='index', sess=get_sessionid(), hosts=h)
