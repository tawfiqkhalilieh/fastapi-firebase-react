from app.database import firebase
from app.models.constants import collection

def delete_all_users():
    docs = firebase.database.collection(u'{collection}'.format(collection=collection))
    db = docs.stream()
    ids = []
    for doc in db:
        ids.append(doc.id)
        docs.document(u'{id}'.format(id=doc.id)).delete()
    return ids