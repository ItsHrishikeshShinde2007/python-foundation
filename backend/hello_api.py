from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Simply Lovely"}

@app.get("/drivers")
def alldrivers():
    return {
        "name": "Max Verstappen",
        "number": 1,
        "team":"Red Bull Racing Team"
    }