from bottle import Bottle, run, request, response ,route
import bottle

# the decorator 
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


@route('/hello')
@enable_cors
def hello():
    return "Hello World!"

@route('/algorithm', method="GET")
@enable_cors
def query():    #return "Hello Algorithm!"
    param1 = request.query.get("param1")
    param2 = request.query.get("param2")
    return param1+param2

run(host='localhost', port=8081, debug=True )
