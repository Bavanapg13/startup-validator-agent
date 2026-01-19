from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME
from prompts.prompts import MVP_PROMPT

client = Groq(api_key=GROQ_API_KEY)

def plan_mvp(idea):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": MVP_PROMPT.format(idea=idea)}]
    )
    return response.choices[0].message.content
