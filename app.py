from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="SD Test")

@app.route("/mongo")
def hello_mongo():
    ret = ["From", "My", "App"]
    return render_template("mongo.html", title="Mongo Test", ret=ret)

if __name__ == "__main__":
    app.run()