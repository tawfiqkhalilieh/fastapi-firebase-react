from app.database import firebase
from app.models.constants import collection

def patch_user(id: str, username: str = None, email: str = None, password: str = None, age: int = None, gender: str = None, birthday: str = None):
    update: dict = dict()
    if username: update["username"] = username
    if email: update["email"] = email
    if password: update["password"] = password
    if age: update["age"] = age
    if gender: update["gender"] = gender
    if birthday: update["birthday"] = birthday
    firebase.database.collection(u'{collection}'.format(collection=collection)).document(u'{id}'.format(id=id)).update(update)
    return update
    