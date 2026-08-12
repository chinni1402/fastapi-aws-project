from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI AWS Demo",
    description="Simple FastAPI project for AWS deployment",
    version="1.0.0"
)


class User(BaseModel):
    name: str
    email: str


users = [
    {
        "id": 1,
        "name": "Anil",
        "email": "anil@example.com"
    },
    {
        "id": 2,
        "name": "Ravi",
        "email": "ravi@example.com"
    }
]


@app.get("/")
def home():
    return {
        "message": "FastAPI application is running successfully!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/ramana")
def version():
    return {
        "version": "1.0.1",
        "message": "HI Ramana, How are you.  💕"
    }

@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.post("/users")
def create_user(user: User):

    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }