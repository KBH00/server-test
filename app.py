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

@app.route("/upload", methods=["POST"])
def upload():
    global ocr

    if "file" not in request.files:
        return jsonify({"error": "no file"}), 400

    # ⚠️ 여기서 OCR 로딩
    if ocr is None:
        from paddleocr import PaddleOCR
        print("Loading OCR model...")
        ocr = PaddleOCR(lang="korean", use_angle_cls=True)

    return jsonify({"result": "test", "confidence": 1.0})
