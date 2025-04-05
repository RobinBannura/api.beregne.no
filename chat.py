import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def beregn_chat(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Du er en hjelpsom og effektiv kalkulator. Svar kun med resultater og korte forklaringer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content