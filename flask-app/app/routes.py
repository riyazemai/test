from flask import render_template, jsonify
import requests
from app import app

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/fastapi-message')
def get_fastapi_message():
    try:
        response = requests.get('http://fastapi-app:8222/api/v1/')
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

