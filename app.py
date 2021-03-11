import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return 'I have changed the message as required!'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')