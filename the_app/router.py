from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from configurations.base_router import BaseRouter
from .db import Database
from .mongo_model import MongoModel
from .serializer import MyCollectionModel
from bson.objectid import ObjectId

db_client = MongoModel(MyCollectionModel)
router = InferringRouter()


@cbv(router)
class TheAppRouter(BaseRouter):

    @router.get("/")
    async def root(self):
        return await db_client.find_all()

    @router.post("/")
    async def post_sth(self, model:MyCollectionModel):
        return await db_client.insert_one(model)

    @router.get("/{_id}")
    async def get_obj(self, _id):
        filters = {"_id": ObjectId(_id)}
        return await db_client.find_one(filters)

    @router.put("/{_id}")
    async def update_obj(self, _id, model: MyCollectionModel):
        return await db_client.update_one(_id ,model)

    @router.delete("/{_id}")
    async def delete_obj(self, _id:str):
        return await db_client.delete_one(_id)