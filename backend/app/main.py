from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.llm_service import get_health_recommendation
from app.database import log_query, fetch_history
from datetime import datetime

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
    try:
        # Get health recommendation from LLM
        result = get_health_recommendation(data.symptoms)

        # Log the query and result to database
        log_query(data.symptoms, result)

        return {"input": data.symptoms, "result": result}

    except Exception as e:
        # Log failed attempts too (optional)
        error_message = f"Error processing symptoms: {str(e)}"
        log_query(data.symptoms, error_message)

        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/health")
@app.head("/health")
async def health_check():
    """Health check endpoint that accepts both GET and HEAD requests"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Healthcare Symptom Checker",
    }


@app.get("/api/history")
def get_history(limit: int = 10):
    """Optional: Get recent query history (for admin/debugging)"""
    try:
        history = fetch_history(limit)
        return {"history": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch history")
