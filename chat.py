import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def beregn_chat(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Du er en økonomisk kalkulator som alltid gir fullstendige og strukturert økonomiske svar.\n\n"
                        "Hvis brukeren spør om noe som handler om lån, skal du alltid inkludere:\n"
                        "- Terminbeløp per måned\n"
                        "- Renter per måned\n"
                        "- Avdrag per måned\n"
                        "- Totale renter i hele perioden\n"
                        "- Totalkostnad for lånet\n"
                        "- Nominell rente\n"
                        "- Effektiv rente (inkludert termingebyr på 50 kr/mnd)\n\n"
                        "Svar kort og ryddig med linjeskift og punktvis informasjon. Ikke bruk introduksjon eller forklaring.\n"
                        "Skriv på norsk og bruk norske kroner. Avslutt alltid med:\n\n"
                        "'Beregningen er sponset av Househacker.'"
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=600
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Feil ved kall til OpenAI:", e)
        return "Beklager, det oppsto en feil under beregningen."