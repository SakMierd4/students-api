from fastapi import FastAPI 
from config import APP_VERSION

app = FastAPI(title="students-api", version=APP-VERSION)

@app.get("/health")
def health():
    return{"status": "ok"}

@app.get("/students")
def list_students():
<<<<<<< Updated upstream
    return[{"id":1, "name": "Ana"}, {"id":2, "name": "Luis"}]
=======
    return [{"id":1,"name":"John Doe","phone":"123-456-7890"},{"id":2,"name":"Jane Smith","phone":"098-765-4321"}]
>>>>>>> Stashed changes
