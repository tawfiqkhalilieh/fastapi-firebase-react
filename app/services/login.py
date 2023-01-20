from app.database import firebase
from app.models.constants import collection

def login(email: str, password: str):
    doc_ref = firebase.database.collection(u'{collection}'.format(collection=collection))
    res =  doc_ref.where(
        u'email', u'==', u'{email}'.format(email=email)
    ).where(
        u'password', u'==', u'{password}'.format(password=password)
    )
    for document in res.stream():
        return { **document.to_dict(), "id": document.id }