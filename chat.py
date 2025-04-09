import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

# Last inn API-nøkkelen
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def beregn_chat(prompt):
    try:
        # Bruk GPT-4 med en instruktiv prompt og et brukerspørsmål
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Du er en ekstremt presis kalkulator med spesialisering innen finans, bolig, bil, energi og lønn. "
                        "Svar kun på konkrete beregninger. Svarene skal være korte, presise og fokusert på tall, ikke forklaringer. "
                        "Unngå prat eller introduksjon. Bruk norske kroner som valuta og norsk språk. "
                        "Dersom spørsmålet er uklart eller ikke mulig å beregne uten ytterligere info, be kort om det som mangler."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,  # Lav temperatur for presise og konsise svar
            max_tokens=300
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Feil ved kall til OpenAI:", e)
        return "Beklager, det oppsto en feil under beregningen."