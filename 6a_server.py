from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    text = request.form.get("text")

    if text is None or text.strip() == "":
        return render_template("index.html", error="Invalid input")

    result = emotion_detector(text)

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return render_template("index.html", result=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
