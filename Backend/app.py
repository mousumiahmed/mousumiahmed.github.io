from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'chatdb'
}

# Connect to MySQL
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/')
def home():
    return "Flask is connected to MySQL!"

@app.route('/urls', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dataUrls")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/add-url', methods=['POST'])
def add_user():
    data = request.get_json()
    url = data.get('url')
    # created_at = data.get('created_at')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dataUrls (url) VALUES (%s)", (url,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'User added successfully!'})

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)
