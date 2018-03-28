# coding: UTF-8
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return u"こんにちは、世界!"

if __name__ == "__main__":
    application.run()
