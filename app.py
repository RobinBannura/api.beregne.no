# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from chat import beregn_chat

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")
        print("Mottatt prompt:", prompt)

        if not prompt:
            return jsonify({"result": "Mangler prompt."}), 400

        result = beregn_chat(prompt)

        if not result:
            return jsonify({"result": "Ingen beregning ble returnert."}), 500

        return jsonify({"result": result})

    except Exception as e:
        print("Feil i /chat:", str(e))
        return jsonify({"result": "Beklager, det oppsto en feil under beregningen."}), 500

if __name__ == "__main__":
    app.run(debug=True)
