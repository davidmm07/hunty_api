from fastapi import APIRouter, Response,status
from config.db import conn
from models.user import User, UpdateUser, UserResponse
from schemas.user import userEntity, usersEntity
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_204_NO_CONTENT

from utils.generator import generateUUID4
user = APIRouter()


@user.get('/users', response_model=list[UserResponse], tags=['users'])
def get_all_users():
    return usersEntity(conn.local.user.find())


@user.get('/users/{id}', response_model=UserResponse, tags=['users'])
def get_user_by_id(id: str):
    return userEntity(conn.local.user.find_one({"UserId": id}))


@user.post('/users', response_model=UserResponse, tags=['users'])
def create_user(user: User):
    userResponse = UserResponse(**user.dict(), UserId=generateUUID4())
    id = conn.local.user.insert_one(jsonable_encoder(userResponse)).inserted_id
    user = conn.local.user.find_one({"_id": id})
    return userEntity(user)


@user.patch('/users/{id}', response_model=UserResponse, tags=['users'])
def update_user(id: str, user: UpdateUser):
    stored_item_data = conn.local.user.find_one({"UserId": id})
    stored_item_model = UpdateUser(**stored_item_data)
    update_data = user.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    conn.local.user.find_one_and_update({"UserId": id}, {
        "$set": jsonable_encoder(updated_item)
    })
    return userEntity(conn.local.user.find_one({"UserId": id}))


@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['users'])
def delete_user(id: str):
    conn.local.user.find_one_and_delete({"UserId": id})
    return Response(status_code=HTTP_204_NO_CONTENT)
