import configurations.base_db as base_db
from configurations.base_db import (
    DatabaseConfiguration,
    start_db
)
from .base_mongo_model import BaseMongoModel
from bson.objectid import ObjectId


class MongoModel(DatabaseConfiguration):
    def __init__(self, model: BaseMongoModel):
        self.model = model

    @start_db()
    async def find_all(self) -> list:
        query = base_db.client.MY_COLLECTION.find()
        result = []
        async for qu in query:
            qu["_id"] = str(qu["_id"])
            result.append(qu)

        return result

    @start_db()
    async def find_one(self, filters) -> BaseMongoModel:
        query = await base_db.client.MY_COLLECTION.find_one(filters)
        query["_id"] = str(query["_id"])
        return query

    @start_db()
    async def insert_one(self, model: BaseMongoModel) -> BaseMongoModel:
        result = await base_db.client.MY_COLLECTION.insert_one(model.dict())
        return model

    @start_db()
    async def update_one(self, _id,model: BaseMongoModel) -> BaseMongoModel:
        query = await base_db.client.MY_COLLECTION.update_one({"_id": ObjectId(_id)}, {"$set": dict(model)})
        if query:
            return 1
        return 0

    @start_db()
    async def delete_one(self, _id: str):
        query = await base_db.client.MY_COLLECTION.delete_one({"_id": ObjectId(_id)})
        if query:
            return 1
        else:
            return 0
