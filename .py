import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def beregn_chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Eller "gpt-3.5-turbo" hvis du ønsker lavere kostnad
        messages=[
            {"role": "system", "content": "Du er en nyttig kalkulator-assistent. Svar kort og tydelig."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )
    return response.choices[0].message["content"].strip()