from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import uuid
import hashlib

app = Flask(__name__)

# MongoDB connection (local MongoDB on default port)
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.json

    item_name = data.get("itemName")
    item_description = data.get("itemDescription")
    item_id = data.get("itemId")
    item_uuid = str(uuid.uuid4())
    item_hash = hashlib.sha256((item_name + item_description).encode()).hexdigest()

    todo_item = {
        "itemId": item_id,
        "itemUUID": item_uuid,
        "itemHash": item_hash,
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(todo_item)

    return jsonify({"message": "Item stored successfully ", "data": todo_item}), 201


if __name__ == "__main__":
    app.run(debug=True)
