# ==============================================================================
# PREDICTION SCRIPT
# Author: Abhishek raj
# ==============================================================================
# This script contains the core function for making predictions.
# ==============================================================================

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
import numpy as np
from PIL import Image
import io
from src import config # Import our settings

def predict_from_image(model_path, img_data):
    """
    Loads a trained Keras model and predicts the class of a single image.

    Args:
        model_path (str): The full path to the saved .h5 model file.
        img_data (bytes): The image data from a file upload.

    Returns:
        dict: A dictionary containing the prediction details (label, confidence).
    """
    try:
        model = load_model(model_path)
        image = Image.open(io.BytesIO(img_data)).convert('RGB').resize(config.IMAGE_SIZE)
        img_array = keras_image.img_to_array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        label = config.CLASS_LABELS_MAP[predicted_index]
        confidence = predictions[0][predicted_index]
        return {"success": True, "prediction": label, "confidence": float(confidence)}
    except Exception as e:
        return {"success": False, "error": str(e)}
