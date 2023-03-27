from fastapi import APIRouter

from models.expresses_model import Express
from config.database import collection_name

from schemas.expresses_schema import expresses_serializers, express_serializer
from bson import ObjectId

express_api_router = APIRouter()

@express_api_router.get("/hello")
async def get_hello():
    return {"msg":"Hello World"}

# retrieve
@express_api_router.get("/")
async def get_expresses():
    expresses = expresses_serializers(collection_name.find())
    return courses

@express_api_router.get("/{id}")
async def get_express(id: str):
    # return {"test": id}
    return express_serializer(collection_name.find_one({"_id": ObjectId(id)}))


# post
@express_api_router.post("/")
async def create_express(express: Express):
    _id = collection_name.insert_one(dict(express))
    return expresses_serializers(collection_name.find({"_id": _id.inserted_id}))


# update
@express_api_router.put("/{id}")
async def update_express(id: str, express: Express):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(express)
    })
    return courses_serializers(collection_name.find({"_id": ObjectId(id)}))

# delete
@express_api_router.delete("/{id}")
async def delete_express(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}