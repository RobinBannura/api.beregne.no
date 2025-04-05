import os
from openai import OpenAI
from dotenv import load_dotenv

# Last inn miljøvariabler
load_dotenv()

# Koble til OpenAI med API-nøkkel
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Send forespørsel til GPT-4
try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hei, har jeg tilgang til GPT-4?"}]
    )
    print("✅ Svar fra GPT-4:", response.choices[0].message.content)
except Exception as e:
    print("❌ Feil:", e)