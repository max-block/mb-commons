from typing import Optional

from pydantic import Field
from pymongo import IndexModel

from mb_commons.mongo import MongoCollection, MongoModel, ObjectIdStr, parse_str_index_model


class Data(MongoModel):
    __collection__ = "data"
    __indexes__ = ["!name"]
    id: Optional[ObjectIdStr] = Field(None, alias="_id")
    name: str


def test_wrap_object_id(mongo_database):
    # with wrapper
    class Data1(MongoModel):
        id: Optional[ObjectIdStr] = Field(None, alias="_id")
        name: str

    coll = MongoCollection(Data1, mongo_database, "data1")
    assert coll.wrap_object_id

    # without wrapper
    class Data2(MongoModel):
        id: Optional[int] = Field(None, alias="_id")
        name: str

    coll = MongoCollection(Data2, mongo_database, "data2")
    assert not coll.wrap_object_id


def test_mongo_model_init_collection(mongo_database):
    col: MongoCollection[Data] = Data.init_collection(mongo_database)
    col.insert_one(Data(name="n1"))
    col.insert_one(Data(name="n2"))
    assert col.count({}) == 2


def test_parse_str_index_model():
    assert IndexModel("k").document == parse_str_index_model("k").document
    assert IndexModel("k", unique=True).document == parse_str_index_model("!k").document
    assert IndexModel([("a", 1), ("b", -1)], unique=True).document == parse_str_index_model("!a,-b").document
