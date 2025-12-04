from flask import Flask, jsonify, request
import os

app = Flask(__name__)

ocr = None  # lazy load

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/")
def home():
    return jsonify({"message": "Server is running"}), 200

