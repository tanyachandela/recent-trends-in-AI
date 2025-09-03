from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)
CORS(app)  # <--- allow frontend to call backend

# Load model (relative path)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.h5")
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Put model.h5 in backend/")

model = tf.keras.models.load_model(MODEL_PATH)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    try:
        img = Image.open(io.BytesIO(file.read())).convert("L").resize((28, 28))
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)  # note: model expects (1,28,28,1)
        preds = model.predict(img_array)
        class_idx = int(np.argmax(preds[0]))
        result = class_names[class_idx]
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)