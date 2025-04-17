from flask import Flask, request, jsonify
from langdetect import detect

app = Flask(__name__)

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

@app.route('/detect', methods=['POST'])
def detect_language():
    data = request.get_json()
    text = data.get('text', '')
    result = {'is_english': is_english(text)}
    return jsonify(result)

@app.route('/')
def home():
    return "Language Detection API is running!"

if __name__ == '__main__':
    app.run()
