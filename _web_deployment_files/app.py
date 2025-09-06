# ==============================================================================
# STREAMLIT WEB APPLICATION (UPGRADED WITH CAMERA INPUT)
# Author: Abhishek raj
# ==============================================================================
# This script launches the user-facing web application, now with two modes:
# 1. File Upload
# 2. Live Camera Capture
# ==============================================================================

import streamlit as st
from PIL import Image
import os
import sys
import io

# Add the 'src' directory to the Python path to import our modules
sys.path.append(os.path.abspath(os.path.join('.', 'src')))
from predict import predict_from_image
from config import MODELS_PATH, FINE_TUNED_MODEL_NAME

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Utensil Classifier AI",
    page_icon="🍽️",
    layout="centered"
)

# --- SIDEBAR ---
st.sidebar.title("About the Project")
st.sidebar.info(
    "This is an AI-powered application that classifies images of utensils "
    "into three categories: 'spoon', 'fork', or 'others'.\n\n"
    "It uses a deep learning model (MobileNetV2) that has been fine-tuned "
    "for high accuracy."
)
st.sidebar.title("Author")
st.sidebar.success("Abhishek raj")


# --- MAIN PAGE ---
st.title("🍽️ Utensil Classifier AI")
st.write(
    "How to use: Choose a tab below to either upload an image or take a new one with your camera."
)

# Define the path to our best model
MODEL_PATH = os.path.join(MODELS_PATH, FINE_TUNED_MODEL_NAME)

# --- HELPER FUNCTION ---
# We create this function to avoid repeating the prediction and display code
def process_and_predict(image_bytes):
    """
    Takes image data in bytes, displays it, and prints the model's prediction.
    """
    st.image(image_bytes, caption='Your Image', use_column_width=True)
    
    with st.spinner('Thinking...'):
        result = predict_from_image(MODEL_PATH, image_bytes)
    
    if result["success"]:
        prediction = result['prediction'].capitalize()
        confidence = result['confidence']
        
        if prediction == 'Spoon':
            st.success(f"### Prediction: Spoon 🥄")
        elif prediction == 'Fork':
            st.success(f"### Prediction: Fork 🍴")
        else:
            st.info(f"### Prediction: Other / None of them 🤔")
        
        st.metric("Confidence", f"{confidence:.2%}")
    else:
        st.error(f"An error occurred during prediction: {result['error']}")


# --- TABS FOR USER CHOICE ---
tab1, tab2 = st.tabs(["📁 Upload an Image", "📸 Capture with Camera"])

# --- UPLOAD TAB ---
with tab1:
    st.header("Upload an image from your device")
    uploaded_file = st.file_uploader("Select an image...", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    
    if uploaded_file is not None:
        # Get the image data in bytes
        image_bytes = uploaded_file.getvalue()
        # Call our helper function to process the image
        process_and_predict(image_bytes)

# --- CAMERA TAB ---
with tab2:
    st.header("Use your camera to take a picture")
    # This is the new camera widget
    camera_image = st.camera_input("Point your camera at a utensil and click the button!", label_visibility="collapsed")
    
    if camera_image is not None:
        # Get the image data in bytes
        image_bytes = camera_image.getvalue()
        # Call our helper function to process the image
        process_and_predict(image_bytes)
