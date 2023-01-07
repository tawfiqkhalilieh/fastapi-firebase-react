from app.database import firebase
from app.models.constants import collection

def update_user(id: str,username: str, email: str, password: str, age: int, gender: str, birthday: str):
    firebase.database.collection(u'{collection}'.format(collection=collection)).document(u'{id}'.format(id=id)).set(
        {
            "username": username,
            "email": email,
            "password": password,
            "age": age,
            "gender": gender,
            "birthday": birthday,
        }
    )
    return {
            "id": id,
            "username": username,
            "email": email,
            "password": password,
            "age": age,
            "gender": gender,
            "birthday": birthday,
        }
