def vacancyEntity(item) -> dict:
    return {
        "PositionName": item["PositionName"],
        "CompanyName": item["CompanyName"],
        "Salary": item["Salary"],
        "Currency": item["Currency"],
        "VacancyId": item["VacancyId"],
        "VacancyLink": item["VacancyLink"],
        "RequiredSkills": item["RequiredSkills"],
    }

def vacanciesEntity(entity) -> list:
    return [vacancyEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]