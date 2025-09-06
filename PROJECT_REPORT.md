#
# Project Report: AI-Powered Utensil Classifier
#

| **Author** | Abhishek raj                               |
|--------------|--------------------------------------------|
| **Date** | September 2025                             |
| **Location** | Bareilly, Uttar Pradesh, India             |
| **Project** | PhD Project Work                           |

---

### **1. Project Objective**

The primary objective of this project was to develop an accurate and reliable multi-class image classifier capable of distinguishing between images of spoons, forks, and other non-utensil objects ("none of them"). The secondary objective was to build this system using a professional, modular, and reproducible software engineering workflow, culminating in an interactive application for real-time prediction.

---

### **2. Dataset**

The project utilized a custom-built image dataset comprised of three distinct classes:

* **`spoon`**: Images containing one or more spoons in various orientations, lighting conditions, and settings.
* **`fork`**: Images containing one or more forks.
* **`others`**: This is the crucial "negative" class, designed to make the model robust. It contains a diverse set of images that are not spoons or forks, including other kitchen items (knives, plates, cups), household objects (keys, pens), animals, and random backgrounds.

Each class was populated with approximately 40-50 images to form the initial dataset.

---

### **3. Methodology: Key Methods Used**

The project was executed following a structured, end-to-end machine learning pipeline.

#### **3.1. Professional Project Environment**
-   **Permanent Workspace:** The entire project was developed within a permanent folder structure on Google Drive, managed via a Google Colab notebook. This solved the issue of temporary session storage and ensured all work was saved and persistent.
-   **Modular Code Structure:** All Python code was organized into a `src/` directory, separating concerns into distinct modules (`config.py` for settings, `predict.py` for inference logic, and `utils.py` for high-level orchestration classes). This follows the **DRY (Don't Repeat Yourself)** principle and makes the code highly maintainable.

#### **3.2. Data Preprocessing & Augmentation**
-   **Keras `ImageDataGenerator`** was used to load images from the directories.
-   To overcome the small dataset size and prevent overfitting, a comprehensive **data augmentation** strategy was employed on the training set. This included random transformations such as:
    -   Rotation
    -   Width and Height Shifting
    -   Shearing
    -   Zooming
    -   Horizontal Flipping
    -   Brightness Adjustment

#### **3.3. Model Architecture & Transfer Learning**
-   The core of the classifier is a **Convolutional Neural Network (CNN)**.
-   **Transfer Learning** was selected as the primary modeling technique to leverage the power of a large, pre-trained model.
-   **MobileNetV2** (pre-trained on the ImageNet dataset) was used as the base model. Its convolutional layers were initially frozen to act as a powerful feature extractor.
-   A **custom classification head** was added on top of the MobileNetV2 base, consisting of:
    1.  `GlobalAveragePooling2D`: To flatten the features.
    2.  `Dropout(0.5)`: A regularization technique to reduce overfitting.
    3.  `Dense(3, activation='softmax')`: The final output layer with 3 neurons (one for each class) and a softmax activation function to output a probability distribution.

#### **3.4. Model Training and Optimization**
A two-stage training process was used to achieve the highest possible accuracy.
1.  **Baseline Training:** The model was first trained for 25 epochs with the MobileNetV2 base layers frozen. This quickly trained the custom head to classify the utensils.
2.  **Fine-Tuning:** After the initial training, the top layers of the MobileNetV2 base (from layer 100 onwards) were "unfrozen." The model was then trained for an additional 15 epochs with a very **low learning rate (1e-5)**. This critical step allowed the model to slightly adjust the pre-trained feature detectors to be more specific to the task, significantly boosting performance.
-   **Learning Rate Scheduling (`ReduceLROnPlateau`)** was also used to automatically decrease the learning rate if the validation loss stopped improving, preventing the model from getting stuck.

#### **3.5. Application & Execution**
-   The final deliverable is an interactive application built directly within a Jupyter/Colab notebook using the **`ipywidgets`** library.
-   The entire project workflow is managed by two custom classes in `src/utils.py`:
    -   `ProjectOrchestrator`: Handles environment setup, file verification, and launching the app.
    -   `GitManager`: Automates the process of pushing the project to GitHub.
-   This object-oriented approach allows the entire project to be set up and run with just a few high-level commands.

---

### **4. Key Findings & Results**

1.  **High Classification Accuracy:** The fine-tuning process was extremely effective. The final, optimized model consistently achieved a high validation accuracy, typically **exceeding 95%**. This demonstrates that a well-structured transfer learning approach can yield excellent results even with a relatively small dataset.
2.  **Importance of the "Others" Class:** The model proved highly effective at rejecting images that were not spoons or forks, correctly classifying them as "others". This confirms the critical importance of having a diverse negative class for building a robust, real-world classifier.
3.  **Workflow Efficiency:** The class-based, modular structure proved to be highly efficient, turning a complex series of steps into a few simple commands. This makes the project easy to reproduce and build upon.

---

### **5. Conclusion & Future Work**

This project successfully met its objective to design, build, and test a high-accuracy utensil classifier. By employing professional software engineering practices and advanced deep learning techniques like fine-tuning, the final model is both powerful and reliable.

Potential areas for future work include:
-   **Expanding the Classes:** Adding new categories like "knife", "plate", or even "spork".
-   **Increasing the Dataset Size:** Gathering more images for each class to further improve robustness and handle more edge cases.
-   **Web Deployment:** Using the `app.py` file to deploy the model as a public web application on a service like Streamlit Community Cloud.
-   **Experimenting with Other Architectures:** Testing other pre-trained models like `EfficientNet` or `ResNet` to compare performance.
