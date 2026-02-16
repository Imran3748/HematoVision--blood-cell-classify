** 🩸 HematoVision – Blood Cell Classification using Transfer Learning (MobileNetV2)**
Python • TensorFlow • Keras • NumPy • Matplotlib • OpenCV

🧬 HematoVision – Blood Cell Type Prediction Feb 2026

📌 Project Description
HematoVision is a deep learning–based blood cell classification system that uses Transfer Learning with MobileNetV2 to automatically identify different types of blood cells from microscopic images.
The system is designed to assist medical professionals by providing fast, accurate, and automated blood cell subtype detection.

**🎯 Project Goal**

The goal of this project is to develop an intelligent automated system capable of classifying blood cell subtypes using deep learning techniques.

The dataset consists of 12,500 augmented microscopic images of blood cells categorized into four major classes:

🔴 Eosinophil

🟢 Lymphocyte

🔵 Monocyte

🟣 Neutrophil

The project leverages a pre-trained MobileNetV2 model and applies the concept of Transfer Learning to build a high-accuracy classification system.

**🏗️ Project Overview:**

The project consists of the following steps:

1️⃣ Data Acquisition

The dataset is downloaded from Kaggle and organized into training and validation directories.

2️⃣ Data Preprocessing

Image resizing to 224x224

Normalization

Data Augmentation using ImageDataGenerator

Rotation

Zoom

Horizontal flip

Shear transformation

3️⃣ Build Pretrained Model

Load MobileNetV2 with ImageNet weights

Freeze base layers

Add custom classification layers:

Global Average Pooling

Dense Layer

Dropout

Output Softmax Layer

4️⃣ Model Training

Optimizer: Adam

Loss Function: Categorical Crossentropy

Metrics: Accuracy

Early Stopping applied to prevent overfitting

5️⃣ Model Evaluation

The trained model is evaluated using:

Validation Accuracy

Loss Curves

Classification Report

Confusion Matrix

▶️ Run the Project

Execute the Jupyter Notebook in sequence:

Load Dataset

Preprocess Data

Build Model

Train Model

Evaluate Model

**📊 Results**

✅ Validation Accuracy: 94% – 96%

Stable training and validation curves

Minor misclassification observed between neutrophils and monocytes

**Observations:**

Some test samples may contain mislabeled images.

Variations in staining and microscope quality may affect accuracy.

Confusion matrix shows slight overlap in morphologically similar classes.

**🧾 Conclusion**

HematoVision demonstrates how Transfer Learning with MobileNetV2 can be effectively applied to medical image classification.

The system achieves high accuracy and proves that deep learning can assist in hematology diagnostics by:

Reducing manual effort

Increasing diagnostic speed

Supporting laboratory professionals
