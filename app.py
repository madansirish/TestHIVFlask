from flask import Flask

app = Flask(__name__)


@app.route('/')
def praful_rathore():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
