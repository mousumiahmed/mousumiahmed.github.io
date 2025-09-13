from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from urllib.parse import quote_plus
username = "mousumiara.ahmed@gmail.com"
password = "Mousumi@123"
username_encoded = quote_plus(username)
password_encoded = quote_plus(password)


import os

app = Flask(__name__)
CORS(app)

# MongoDB connection
# MONGO_URI = os.environ.get("mongodb+srv://mousumi:<mousumi@123>@cluster0.00x9tl4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# client = MongoClient(MONGO_URI)
MONGO_URI = "mongodb+srv://{username_encoded}:{password_encoded}@cluster0.00x9tl4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)

db = client.get_database('chatdb')
collections = db.list_collection_names()
print("Collections in the database:", collections)


db = client['chatdb']
# messages = db['messages']
chaturls = db['chaturls']


@app.route('/')
def home():
    return "Home Page"

# @app.route('/api/chaturl', methods=['POST'])
# def index():
#      data = request.json
#      chaturl = data.get('chaturl')   
#      if not chaturl:
#          return jsonify({"error": "Missing chaturl"}), 400

#      chaturls.insert_one({ "chaturl": chaturl })
#      return jsonify({"status": "Chat URL saved"}), 200

@app.route('/api/chat', methods=['GET'])
def get_url():
    # Retrieve all documents from the 'chaturls' collection, excluding '_id'
    msgs = list(chaturls.find({}, {'_id': 0}))
    
    # Optional: print the result for debugging
    print(msgs)

    return jsonify(msgs)

     

# @app.route('/api/chat', methods=['POST'])
# def save_message():
#     data = request.json
#     timestamp = data.get('timestamp')
#     sender = data.get('sender')
#     message = data.get('message')

#     if not all([timestamp, sender, message]):
#         return jsonify({"error": "Missing fields"}), 400

#     messages.insert_one({
#         "timestamp": timestamp,
#         "sender": sender,
#         "message": message
#     })
#     return jsonify({"status": "Message saved"}), 200

# @app.route('/api/chat', methods=['GET'])
# def get_messages():
#     msgs = list(messages.find({}, {'_id': 0}))
#     return jsonify(msgs)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
