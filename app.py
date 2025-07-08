from flask import Flask, render_template
from pymongo import MongoClient

# atlas connection
atlas_connection = "mongodb+srv://sderi:Walter42@atlasfrgbaalprod.ghyic.mongodb.net/"
atlas_db = 'BaalSystemMonitoring'

client = MongoClient(atlas_connection)
db = client[atlas_db]

# collections
col = db['monitor']

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="SD Test")

@app.route("/mongo")
def hello_mongo():
    ret = col.find_one({"name" : "MAPPS"})
    return render_template("mongo.html", title="Mongo Test", ret=ret)

if __name__ == "__main__":
    app.run()