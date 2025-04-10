import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

# Last inn API-nøkkelen
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
                        "Du er en økonomisk kalkulator som gir ryddige, punktvise og presise svar på norske. "
                        "Svar alltid med linjeskift og punktliste, og aldri med innledning, forklaring eller spørsmål tilbake. "
                        "Svar skal fokusere på tall og være skrevet som en kort rapport. Bruk norske kroner. "
                        "Hvis spørsmålet handler om lån, skal følgende alltid vises – hver på egen linje:\n"
                        "- Terminbeløp per måned\n"
                        "- Renter per måned (første måned)\n"
                        "- Avdrag per måned (første måned)\n"
                        "- Totale renter i hele perioden\n"
                        "- Totalkostnad for lånet\n"
                        "- Nominell rente\n"
                        "- Effektiv rente (inkludert termingebyr på 50 kr/mnd)\n\n"
                        "Formatér svaret som en punktliste med linjeskift.\n"
                        "Avslutt alltid med:\n\nBeregningen er sponset av Househacker."
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