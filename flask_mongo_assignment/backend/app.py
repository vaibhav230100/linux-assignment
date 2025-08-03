from flask import Flask, jsonify, request
from pymongo import MongoClient
import json
from flask_cors import CORS
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)

MONGO_URL = os.getenv("MONGO_URL")
if not MONGO_URL:
    raise ValueError("MONGO_URL is not set in .env file")


client = MongoClient(MONGO_URL)
db = client["flask_assignment"]
collection = db["users"]


@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")

        if not name or not email:
            return jsonify({"error": "All fields are required"}), 400

        collection.insert_one({"name": name, "email": email})
        return jsonify({"message": "Data submitted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
