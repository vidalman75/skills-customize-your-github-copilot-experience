from fastapi import FastAPI

app = FastAPI(title="FastAPI REST API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Welcome to your FastAPI assignment!"}
