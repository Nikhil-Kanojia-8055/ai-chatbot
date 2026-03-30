from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_msg = request.json.get("message")
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

app.run(debug=True)