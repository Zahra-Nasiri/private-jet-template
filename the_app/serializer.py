from .base_mongo_model import BaseMongoModel

class MyCollectionModel(BaseMongoModel):
    name: str
    age: int
