from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME
from prompts.prompts import MARKET_ANALYSIS_PROMPT

client = Groq(api_key=GROQ_API_KEY)

def analyze_market(idea):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": MARKET_ANALYSIS_PROMPT.format(idea=idea)}]
    )
    return response.choices[0].message.content
