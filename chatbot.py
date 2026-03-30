import pickle
import json
import random

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

with open("intents.json", encoding="utf-8") as file:
    data = json.load(file)

def get_response(user_input):
    X = vectorizer.transform([user_input])
    tag = model.predict(X)[0]

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "I didn't understand 😅"