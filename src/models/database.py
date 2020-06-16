import os

from pymongo import MongoClient

db_config = {
    "type": "mongodb",
    "user": os.environ["MONGO_USER"],
    "password": os.environ["MONGO_PASSWORD"],
    "host": "mongo",
    "port": "27017",
    "db": "hf_database",
}


def make_url(db_config, include_db=True):
    url = db_config["type"]
    url += "://" + db_config["user"]
    url += ":" + db_config["password"]
    url += "@" + db_config["host"]
    url += ":" + db_config["port"]
    return url


db_url = make_url(db_config, include_db=False)
print(db_url)
db = MongoClient(db_url)[db_config["db"]]
