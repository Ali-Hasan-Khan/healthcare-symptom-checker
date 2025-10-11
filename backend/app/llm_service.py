from app.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL
from openai import OpenAI

client = OpenAI(
    base_url=f"{OPENROUTER_BASE_URL}",
    api_key=f"{OPENROUTER_API_KEY}",
)

DISCLAIMER = "This is for educational purposes only and not medical advice."


def get_health_recommendation(symptom_text: str) -> str:
    prompt = f"""
    Based on the following symptoms:
    "{symptom_text}"
    Suggest possible conditions and next steps.
    Include this disclaimer: {DISCLAIMER}
    """

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = client.chat.completions.create(
            model=data["model"], messages=data["messages"]
        )
        # print(response.choices[0].message.content)
        return response.choices[0].message.content or ""
    except Exception as e:
        return f"Error contacting LLM API: {str(e)}"


# if __name__ == "__main__":
#     get_health_recommendation("I have fever")
