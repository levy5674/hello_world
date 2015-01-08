from flask import Flask
import os

DEFAULT_PORT = 5000

app = Flask(__name__)

@app.route('/', defaults={'path':'World'})
@app.route('/<path:path>')
def hello_world(path):
    return 'Hello %s!\n' % path

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', DEFAULT_PORT)))
