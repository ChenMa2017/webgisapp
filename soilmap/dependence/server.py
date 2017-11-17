from bottle import Bottle, run, request, response, static_file

app = Bottle()

# Change many values at once
app.config.update({
    'autojson': False,
    'sqlite.db': ':memory:',
    'myapp.param': 'value',
    'app.host':'localhost',
    'app.port':8081
})

@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.get('/<filename:path>', method="GET")
def server_static(filename):
    return static_file(filename, root='D:\webapp\soilmap')


@app.route('/')
def index():
    return static_file('index.html', root='D:\webapp\soilmap')

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/algorithm', method="GET")
def query():    #
    param1 = request.query.get("param1")
    param2 = request.query.get("param2")
    return "Hello Algorithm!"
    
    #return param1+param2


if __name__ == '__main__':
    print app
    app.config.load_config('conf.ini')
    run(app, host=app.config['app.host'], port=app.config['app.port'], debug=True)
