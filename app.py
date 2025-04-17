from flask import Flask, request, jsonify
from langdetect import detect

app = Flask(__name__)

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

@app.route('/detect', methods=['GET'])
def detect_language():
    text = request.args.get('text', '')

    # Remove surrounding quotes if present
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    elif text.startswith("'") and text.endswith("'"):
        text = text[1:-1]

    if not text:
        return jsonify({"error": "Missing or invalid 'text' query parameter"}), 400

    result = {
        "text": text,
        "is_english": is_english(text)
    }
    return jsonify(result)

@app.route('/')
def home():
    return "✅ Language Detector API is running! Use /detect?text=your+text"

if __name__ == '__main__':
    app.run()
