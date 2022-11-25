from fastapi import APIRouter, Response,status
from config.db import conn
from models.vacancy import Vacancy, UpdateVacancy, VacancyResponse
from schemas.vacancy import vacancyEntity, vacanciesEntity
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_204_NO_CONTENT
from utils.generator import generateUUID4
vacancy = APIRouter()


@vacancy.get('/vacancies', response_model=list[VacancyResponse], tags=['vacancies'])
def get_all_vacancies():
    return vacanciesEntity(conn.local.vacancy.find())


@vacancy.get('/vacancies/{id}', response_model=VacancyResponse, tags=['vacancies'])
def get_vacancy_by_id(id: str):
    return vacancyEntity(conn.local.vacancy.find_one({"VacancyId": id}))


@vacancy.post('/vacancies', response_model=VacancyResponse, tags=['vacancies'])
def create_vacancy(vacancy: Vacancy):
    vacancyResponse = VacancyResponse(**vacancy.dict(), VacancyId=generateUUID4())
    id = conn.local.vacancy.insert_one(jsonable_encoder(vacancyResponse)).inserted_id
    vacancy = conn.local.vacancy.find_one({"_id": id})
    return vacancyEntity(vacancy)


@vacancy.patch('/vacancies/{id}', response_model=VacancyResponse, tags=['vacancies'])
def update_vacancy(id: str, vacancy: UpdateVacancy):
    stored_item_data = conn.local.vacancy.find_one({"VacancyId": id})
    stored_item_model = UpdateVacancy(**stored_item_data)
    update_data = vacancy.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    conn.local.vacancy.find_one_and_update({"VacancyId": id}, {
        "$set": jsonable_encoder(updated_item)
    })
    return vacancyEntity(conn.local.vacancy.find_one({"VacancyId": id}))


@vacancy.delete('/vacancies/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['vacancies'])
def delete_vacancy(id: str):
    conn.local.vacancy.find_one_and_delete({"VacancyId": id})
    return Response(status_code=HTTP_204_NO_CONTENT)

