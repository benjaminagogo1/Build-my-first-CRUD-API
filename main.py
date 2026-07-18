

tasks = {
    "id": 1,
    "title": "Buy milk",
    "Done": False
}



[
    {
        "id": 2,
        "title": "studying Go",
        "done": true
    },

    {
        "id": 3,
        "title": "success",
        "done": false
    }
]

@app.get("/tasks")
def get_tasks():

uvicorn main:app --reload


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}