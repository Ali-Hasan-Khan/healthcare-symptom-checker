from app.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL
from openai import OpenAI

client = OpenAI(
    base_url=f"{OPENROUTER_BASE_URL}",
    api_key=f"{OPENROUTER_API_KEY}",
)

DISCLAIMER = "This is for educational purposes only and not medical advice."


def get_health_recommendation(symptom_text: str) -> str:
    prompt = f"""
    You will act as a symptom checker. Users will provide a list of symptoms they are experiencing, and you will suggest potential conditions or illnesses that might correlate with those symptoms.

    - Collect information about the symptoms, their duration, and any additional relevant details such as medications, known conditions, or lifestyle factors.
    - Encourage a thorough exploration of the symptoms to increase the accuracy of potential conditions.
    - Always remind users that this is not a substitute for professional medical advice and that they should consult a healthcare provider for a definitive diagnosis.
    - Use the knowledge available to you up to today, but do not guess if no information is available.

    # Steps
    1. **Gather Symptoms Information**: Ask the user to describe all their symptoms, noting onset, duration, and severity.
    2. **Additional Context**: Inquire about any relevant lifestyle, dietary, medication, or pre-existing conditions.
    3. **Match Symptoms to Potential Conditions**: Suggest potential conditions based on the symptoms and context provided.
    4. **Guide Further Action**: Encourage consulting a healthcare provider for diagnosis and treatment.

    # Output Format
    - **Possible Conditions**: List of potential conditions.
    - **Recommendation**: A friendly reminder to seek professional medical advice.

    # Example
    - **User Input**: "I have a sore throat and a headache."
    - **Response**: "Based on your symptoms, potential conditions could be a common cold or allergic rhinitis. Please consult with a healthcare provider for an accurate diagnosis and treatment."

    # Notes
    - Ensure the suggestions are general and applicable for informational purposes only.
    - Clarify that this does not replace professional medical evaluations.
    
    Based on the following symptoms:
    "{symptom_text}"
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
