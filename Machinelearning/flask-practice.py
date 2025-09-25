from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "WELCOME TO FLASK DEVELOPMENT and we will build regression model"

app.run(host = '127.0.0.10', port=5000)