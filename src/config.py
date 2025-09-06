# ==============================================================================
# CONFIGURATION FILE
# ==============================================================================
# This file contains all the settings and parameters for the project.
# By keeping them here, we make our code clean and easy to modify.
# ==============================================================================

import os

# --- PATHS ---
# This defines the permanent home of your project in Google Drive.
BASE_PATH = "/content/drive/MyDrive/PHD Project/Utensil_Classifier_Project"

# Define other important paths relative to the base path.
DATA_PATH = os.path.join(BASE_PATH, "data")
MODELS_PATH = os.path.join(BASE_PATH, "models")
RESULTS_PATH = os.path.join(BASE_PATH, "results")

# Define the names for our two different trained models.
BASIC_MODEL_NAME = "multiclass_detector_basic.h5"
FINE_TUNED_MODEL_NAME = "multiclass_detector_fine_tuned.h5"

# --- DATA & IMAGE PARAMETERS ---
# Define the size we will resize all images to.
IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224
IMAGE_SIZE = (IMAGE_HEIGHT, IMAGE_WIDTH)

# --- TRAINING PARAMETERS ---
# Define how the model will be trained.
BATCH_SIZE = 8          # How many images to process at once.
INITIAL_EPOCHS = 25     # Number of training cycles for the initial phase.
FINE_TUNE_EPOCHS = 15   # Number of additional training cycles for fine-tuning.
INITIAL_LR = 1e-3       # Initial learning rate (0.001).
FINE_TUNE_LR = 1e-5       # Very low learning rate for fine-tuning (0.00001).
FINE_TUNE_AT = 100        # Which layer of the base model to start unfreezing from.

# --- CLASS MAPPING ---
# Maps the folder index (0, 1, 2) to the actual class name.
CLASS_LABELS_MAP = {0: 'fork', 1: 'others', 2: 'spoon'}
