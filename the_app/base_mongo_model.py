from pydantic import BaseModel
from bson.objectid import ObjectId

class BaseMongoModel(BaseModel):

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
