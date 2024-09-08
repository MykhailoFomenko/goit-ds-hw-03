from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId


client = MongoClient(
    "mongodb+srv://user:12345@cluster0.vcfj7.mongodb.net/", server_api=ServerApi("1")
)

db = client.cats

result_one = db.cats.insert_one(
    {
        "_id": ObjectId("60d24b783733b1ae668d4a77"),
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)


def read_from_collection_by_name(collection, name: str) -> dict:
    """
    Funtion of printing info about cat by his/her name
    Input:
    :param collection
    :param name: string

    Output:
    :print: dict
    """
    result = collection.find_one({"name": name})
    print(result)


def read_all_from_collection(collection) -> dict:
    """
    Funtion of printing all info from collection
    Input:
    :param collection

    Output:
    :print: dict
    """
    result = collection.find({})
    for el in result:
        print(el)


def update_age_by_name(collection, name: str, age: int) -> None:
    """
    Funtion of updating age of cat by name
    Input:
    :param collection
    :param name: string
    :param age: integer

    Output:
    ::
    """
    collection.update_one({"name": name}, {"$set": {"age": age}})


def update_features_by_name(collection, name: str, new_feature: str) -> None:
    """
    Funtion of updating list of features of cat by name
    Input:
    :param collection
    :param name: string
    :param new_feature: string

    Output:
    ::
    """
    collection.update_one({"name": name}, {"$addToSet": {"features": new_feature}})


def delete_by_name(collection, name: str) -> None:
    """
    Funtion of deleting records from collection by name
    Input:
    :param collection
    :param name: string

    Output:
    ::
    """
    collection.delete_one({"name": name})


def delete_all(collection) -> None:
    """
    Funtion of deleting all records from collection
    Input:
    :param collection

    Output:
    ::
    """
    collection.delete_many({})


try:
    read_from_collection_by_name(db.cats, "barsik")
    read_all_from_collection(db.cats)
    update_age_by_name(db.cats, "barsik", 5)
    update_features_by_name(db.cats, "barsik", "Носиться по хаті в 3 години ночі")
    delete_by_name(db.cats, "barsik")
    delete_all(db.cats)
except Exception as e:
    print(e)
