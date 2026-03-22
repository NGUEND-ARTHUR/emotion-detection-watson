from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotion")
def emotion():
    text = request.args.get("text")

    if not text or text.strip() == "":
        return jsonify({
            "error": "400 Bad Request",
            "message": "Input text cannot be empty"
        }), 400

    result = emotion_detector(text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
