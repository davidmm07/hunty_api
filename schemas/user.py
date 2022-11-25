def userEntity(item) -> dict:
    return {
        "UserId": item["UserId"],
        "FirstName": item["FirstName"],
        "LastName": item["LastName"],
        "Email": item["Email"],
        "YearsPreviousExperience": item["YearsPreviousExperience"],
        "Skills": item["Skills"],
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]