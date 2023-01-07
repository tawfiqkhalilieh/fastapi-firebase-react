from app.database import firebase
from app.models.constants import collection

def get_all_users():
    docs = firebase.database.collection(u'{collection}'.format(collection=collection)).stream()
    users = []
    for doc in docs:
        users.append({ doc.id : doc.to_dict()})
    return users