# PyMIP - Python Medical Image Processing 🩺

An open-source repository for exploring and developing solutions in Medical Image Processing, from classic filtering techniques to Machine Learning applications.

![Painel de Análise de Fratura](URL_DO_PAINEL_2X2_AQUI)

## 🚀 About This Project

This repository documents my hands-on journey into the world of Medical Image Processing. What started as a fundamental study of pixel manipulation has evolved into the development of practical analysis tools and intelligent systems. The projects here demonstrate a workflow that encompasses research, experimentation, implementation, and documentation.

## ✨ Key Features & Implemented Techniques

This project showcases a wide range of implemented techniques, including:

* **Classic Image Processing:**
    * Brightness/Contrast adjustment, Image Inversion, and Cropping.
    * **Contrast Enhancement:** Histogram Analysis, global Histogram Equalization (`equalizeHist`), and the more advanced **Adaptive Histogram Equalization (CLAHE)**.
    * **Image Filtering:** Application of smoothing filters (`GaussianBlur`, `MedianBlur`) for noise reduction and sharpening filters with custom **Convolution Kernels**.
    * **Edge Detection:** Implementation of classic algorithms like `Sobel` and the industry-standard `Canny` edge detector.

* **Machine Learning:**
    * **Complete ML Pipeline:** Demonstrated the full workflow, including dataset creation, feature extraction, model training, and validation.
    * **Image Classification:** Trained a **Support Vector Machine (SVM)** classifier using Scikit-learn to automatically identify image properties based on extracted features (like histograms).

## 🔬 Case Studies (Featured Projects)

### 1. Fracture Analysis Optimizer

A proof-of-concept tool designed to assist in medical diagnosis by generating a dashboard of multiple, optimized views from a single X-ray. Each view uses a different processing pipeline to highlight specific features:

* **General Contrast View (CLAHE):** For overall anatomical context.
* **Contour View (Canny):** To isolate bone outlines and clearly identify structural breaks (fractures).
* **Fine Detail View (Inverted+CLAHE):** A custom technique to enhance details within dense structures like bone.

### 2. Intelligent Noise Pre-processor

An innovative system that automates a critical pre-processing step. This project stemmed from the hypothesis that an image's histogram can be used as a "fingerprint" to diagnose the type of noise it contains.

An SVM model was trained on a dataset of histograms from images with different noise types. **The model achieved 100% accuracy** on the test set, successfully proving it can automatically choose the correct noise-reduction filter (`GaussianBlur` vs. `MedianBlur`) for an input image.

![Resultado da Acurácia do Modelo](URL_DA_IMAGEM_DE_100%_AQUI)

* `[Read the full technical analysis for this project here](./docs/smart-preprocessor-analysis.md)`

## 🛠️ Technologies Used

* **Language:** Python
* **Core Libraries:**
    * OpenCV-Python
    * NumPy
    * Matplotlib
    * Scikit-learn

## 🔮 Project Roadmap

* [x] ~~Implement contrast enhancement filters (Histogram Equalization).~~ (Concluído!)
* [x] ~~Explore automatic image segmentation techniques.~~ (Concluído com Detecção de Bordas!)
* [x] ~~Introduce Machine Learning algorithms for diagnostic classification.~~ (Concluído com o Classificador de Ruído!)
* [ ] **(Next Step)** Dive into **Deep Learning (Module 6)**, building Convolutional Neural Networks (CNNs) to allow the AI to learn features automatically from raw pixels.
* [ ] Apply Deep Learning to a real-world problem, such as pneumonia classification or tumor segmentation.

---
*This project is being developed with guidance from Gemini AI.*
