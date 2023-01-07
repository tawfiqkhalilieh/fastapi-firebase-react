## FastAPI Firebase Task

<hr>
## Running

```shell
$ python -m venv env
$ source env/Scripts/activate
$ pip install -r requirements.txt
$ uvicorn app.main:app --relaod
```

## Task:

- your task is to create a database application for sign-up/log-in
- overall the functionality that should be included is:
  - [x] Login in
  - [x] Sign up
  - [x] Change password
  - [x] Change username/email
  - [x] get user details
  - [x] get all users (this should have an authorization check)
  - [x] delete user
  - [x] Delete all users
- The technology you will use is:
  - FastAPI
  - Firebase
- Each user should have at least the following:
  - Username
  - Email
  - Password
  - Age
  - Birthday
  - Gender
- Note:
  - You need to create the database using Firestore
  - You need to create all of the Models using Pydantic
