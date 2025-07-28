from flask import Flask, request, jsonify, render_template
from PIL import Image
import pytesseract
from flask_cors import CORS

# ⚠️ අයින් කරලා තියෙන්නෙ Run Termux නම් ඇඩ් කරපන් 
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    image = Image.open(file.stream)

    # ⚠️ Sinhala Language OCR
    extracted_text = pytesseract.image_to_string(image, lang='sin+eng')

    return jsonify({'extracted_text': extracted_text})

import os

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
