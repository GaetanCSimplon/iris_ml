from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict/")
def predict():
    pass
    