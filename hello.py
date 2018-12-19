from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Let me guess. You have a great personality."
