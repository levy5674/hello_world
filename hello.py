from flask import Flask
import os

DEFAULT_PORT = 5000

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', DEFAULT_PORT)))
