from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    text = request.args.get('text')

<<<<<<< HEAD
    # Gestion input vide
=======
>>>>>>> 058ee90 (Final project submission with all fixes)
    if text is None or text.strip() == "":
        return "Invalid input! Try again."

    result = emotion_detector(text)

<<<<<<< HEAD
    # Si erreur (ex: API)
    if "error" in result:
        return "Invalid input! Try again."

    # Format EXACT attendu par IBM
=======
    if "error" in result:
        return "Invalid input! Try again."

>>>>>>> 058ee90 (Final project submission with all fixes)
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
