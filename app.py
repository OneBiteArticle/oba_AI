from fastapi import FastAPI

app = FastAPI(title="OBA AI Service")

@app.get("/")
def health_check():
    return {"status": "OK", "message": "OBA AI Service is running"}
