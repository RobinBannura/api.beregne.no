from dotenv import load_dotenv
import os
import openai
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from chat import beregn_chat

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Velkommen til API for Beregne.no"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt mangler"}), 400

    try:
        response = beregn_chat(prompt)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

if __name__ == "__main__":
    app.run(debug=True)