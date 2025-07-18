from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

from flask import send_from_directory

@app.route("/chat.html")
def chat_page():
    return send_from_directory('.', 'chat.html')

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json.get("message")
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "너는 마이크로디그리 챗봇이다. 간단하게 답하라."},
            {"role": "user", "content": user_msg}
        ]
    )
    return jsonify({"answer": response.choices[0].message.content})

@app.route("/")
def hello():
    return "마이크로디그리 챗봇 서버 정상동작 중!"

"""
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
"""
