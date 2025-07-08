from pymongo import MongoClient

# atlas connection
atlas_connection = "mongodb+srv://sderi:Walter42@atlasfrgbaalprod.ghyic.mongodb.net/"
atlas_db = 'BaalSystemMonitoring'

client = MongoClient(atlas_connection)
db = client[atlas_db]

# collections
col = db['monitor']

ret = col.find_one({"name" : "MAPPS"})
for i in ret:
    print(i)