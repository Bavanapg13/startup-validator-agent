from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME
from prompts.prompts import FEATURE_PROMPT

client = Groq(api_key=GROQ_API_KEY)

def generate_features(idea):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": FEATURE_PROMPT.format(idea=idea)}]
    )
    return response.choices[0].message.content
