from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Class names (change according to your dataset)
CLASS_NAMES = ['Eosinophil', 'Lymphocyte', 'Monocyte', 'Neutrophil']

IMG_SIZE = 224

def load_model():
    try:
        import tensorflow as tf
        MODEL_PATH = "C:/temp/image_model.keras"
        return tf.keras.models.load_model(MODEL_PATH)
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def preprocess_image(image):
    try:
        import numpy as np
        from PIL import Image
        image = image.resize((IMG_SIZE, IMG_SIZE))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)
        return image
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    from PIL import Image
    image = Image.open(file).convert("RGB")

    model = load_model()
    if model is None:
        return jsonify({"error": "Model loading failed"}), 500

    processed_image = preprocess_image(image)
    if processed_image is None:
        return jsonify({"error": "Image preprocessing failed"}), 500

    import numpy as np
    predictions = model.predict(processed_image)
    confidence = float(np.max(predictions))
    class_index = np.argmax(predictions)

    return jsonify({
        "prediction": CLASS_NAMES[class_index],
        "confidence": round(confidence * 100, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
