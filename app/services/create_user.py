from app.database import firebase
from app.models.constants import collection

def create_user(id: str,username: str, email: str, password: str, age: int, gender: str, birthday: str):
    firebase.database.collection(u'{collection}'.format(collection=collection)).document(u'{id}'.format(id=id)).set({
        u'username': u'{username}'.format(username=username),
        u'email': u'{email}'.format(email=email),
        u'password': u'{password}'.format(password=password),
        u'age': u'{age}'.format(age=age),
        u'gender': u'{gender}'.format(gender=str(gender)),
        u'birthday': u'{birthday}'.format(birthday=birthday)
    })
    
    return {
        'id': id,
        'username': '{username}'.format(username=username),
        'email': '{email}'.format(email=email),
        'password': '{password}'.format(password=password),
        'age': '{age}'.format(age=age),
        'gender': '{gender}'.format(gender=str(gender)),
        'birthday': '{birthday}'.format(birthday=birthday)
    }