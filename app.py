from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Team! Welcome to Test HIV application using Flask.</h1>'

if __name__ == '__main__':
    app.run(debug= True, port= 5004)
