import re

from app.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL
from openai import OpenAI

client = OpenAI(
    base_url=f"{OPENROUTER_BASE_URL}",
    api_key=f"{OPENROUTER_API_KEY}",
)

DISCLAIMER = "This is for educational purposes only and not medical advice."


def normalize_response_format(response: str) -> str:
    """Normalize the LLM response to ensure consistent formatting"""

    # Remove extra whitespace and normalize line breaks
    response = re.sub(r"\n\s*\n\s*\n+", "\n\n", response)
    response = response.strip()

    # Ensure consistent heading format
    response = re.sub(r"\*\*([^*]+)\*\*\s*:?\s*", r"**\1:**\n\n", response)

    # Normalize bullet points
    response = re.sub(r"^\s*[\-•]\s*", "- ", response, flags=re.MULTILINE)

    # Ensure proper spacing after headings
    response = re.sub(r"(\*\*[^*]+\*\*:)\n([^\n])", r"\1\n\n\2", response)

    # Remove excessive spacing
    response = re.sub(r"\n{3,}", "\n\n", response)

    return response


def get_health_recommendation(symptom_text: str) -> str:
    prompt = f"""You are a medical information assistant. You MUST follow this EXACT format with NO deviations:

## STRICT FORMATTING RULES:
1. Use EXACTLY these headings with double asterisks: **Heading Name:**
2. Leave EXACTLY one blank line after each heading
3. Use bullet points with single dashes (-)
4. NO extra formatting, NO bold text except headings
5. Keep each section concise (2-3 sentences max per point)

## REQUIRED RESPONSE FORMAT:

**Symptom Summary**

Brief acknowledgment of the reported symptoms in 1-2 sentences.

**Possible Conditions**

- Condition 1: Brief explanation (most likely)
- Condition 2: Brief explanation (common)
- Condition 3: Brief explanation (less common)

**When to Seek Immediate Care**

- List red flag symptoms requiring urgent care
- Only include if applicable to the symptoms

**General Recommendations**

- Suggest next steps (self-care, doctor visit, etc.)
- Mention symptoms to monitor
- Healthcare provider questions to ask

**Important Disclaimer**
{DISCLAIMER}

## USER'S SYMPTOMS:
"{symptom_text}"

Respond using EXACTLY the format above. Do not add extra formatting or deviate from this structure."""

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a medical assistant that ALWAYS follows the exact formatting provided. Never deviate from the specified structure.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,  # Lower temperature for more consistent responses
    }

    try:
        response = client.chat.completions.create(
            model=data["model"], messages=data["messages"], temperature=0.3
        )
        raw_response = response.choices[0].message.content or ""

        # Apply formatting normalization
        formatted_response = normalize_response_format(raw_response)

        return formatted_response
    except Exception as e:
        return f"Error contacting LLM API: {str(e)}"


# if __name__ == "__main__":
#     get_health_recommendation("I have fever")
