from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Healthcare Symptom Checker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SymptomInput(BaseModel):
    symptoms: str


@app.post("/api/check")
def check_symptoms(data: SymptomInput):
    print("data:", data)
    return {"input": data.symptoms, "result": f"checking symptoms for {data.symptoms}"}
