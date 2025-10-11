from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.llm_service import get_health_recommendation

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
    result = get_health_recommendation(data.symptoms)
    return {"input": data.symptoms, "result": result}
