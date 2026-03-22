import requests

def emotion_detector(text):
    # Gestion du cas input vide (400)
    if text is None or text.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "error": "400 Bad Request"
        }

    try:
        url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

        headers = {
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }

        data = {"raw_document": {"text": text}}

        response = requests.post(url, json=data, headers=headers, timeout=5)

        # Gestion status code 400 venant de l’API
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
                "error": "400 Bad Request"
            }

        result = response.json()

        emotions = result["emotionPredictions"][0]["emotion"]

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }

    except Exception:
        # fallback sécurisé
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "error": "400 Bad Request"
        }
