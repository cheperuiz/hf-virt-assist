import datetime

from models.database import db


def get_all_quotes(collection=db["quotes"]):
    all_quotes = collection.find()
    return all_quotes


def save_quote(quote, collection=db["quotes"]):
    quote["created_at"] = datetime.datetime.now()
    result = collection.insert_one(quote)
    return str(result.inserted_id)
