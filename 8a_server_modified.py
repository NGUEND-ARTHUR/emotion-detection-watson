from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


def analyze_code_style(text):
    if text is None:
        return "Invalid input: None"

    if not isinstance(text, str):
        return "Invalid input type"

    if len(text.strip()) == 0:
        return "Empty input detected"

    return "Code analysis passed"


@app.route("/emotion")
def emotion():
    text = request.args.get("text")

    analysis_result = analyze_code_style(text)

    if analysis_result != "Code analysis passed":
        return jsonify({
            "error": "400 Bad Request",
            "message": analysis_result
        }), 400

    result = emotion_detector(text)

    return jsonify({
        "analysis": analysis_result,
        "result": result
    })


if __name__ == "__main__":
    app.run(debug=True)
