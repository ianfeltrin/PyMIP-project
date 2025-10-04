# Analysis of Medical Image Enhancement using Image Inversion and the CLAHE Technique

*Author: Ian Feltrin*
*Date: October 4, 2025*

---

### 1. Introduction: The Challenge of X-ray Visualization

Diagnostic X-ray images, while fundamental in medicine, often present a challenge: the information can be concentrated in bright, low-contrast areas, making it difficult for the human eye to analyze subtle details continuously. This project explores how digital image post-processing techniques, using Python, can enhance these images to aid in medical diagnosis.

We investigate two primary methods: simple image inversion and a more advanced algorithm, Contrast Limited Adaptive Histogram Equalization (CLAHE), applied to both the original and inverted images.

### 2. Methodology

The following techniques were applied to standard grayscale X-ray images:

* **Image Inversion:** A simple mathematical operation where each pixel's new value is calculated as `255 - original_value`. This effectively turns the image into a photographic negative, making bright areas dark and dark areas bright, which can sometimes improve visual perception in overly bright images.

* **CLAHE (Contrast Limited Adaptive Histogram Equalization):** A sophisticated algorithm from the OpenCV library. Instead of applying one contrast rule to the entire image, CLAHE divides the image into small, localized tiles (or "windows") and enhances the contrast of each tile independently. This "adaptive" nature allows it to bring out details in both dark and light regions of the image without over-saturating the result.

### 3. Results and Analysis

By applying these techniques, we can observe significant differences that suggest distinct use cases for diagnosis.

*(Aqui você pode colocar a sua imagem de 8 plots!)*
`![Análise Comparativa](URL_DA_SUA_IMAGEM_DE_8_PLOTS_AQUI)`

#### 3.1. Standard CLAHE: Enhancing Soft Tissues

Applying CLAHE to the original image significantly improves contrast in less dense regions, such as the lung fields. The resulting image is more "natural" and makes it easier to inspect soft tissue structures.

This enhancement could be crucial for diagnosing conditions like:
* **Pneumonia** (visualizing areas of consolidation or inflammation in the lungs).
* **Lung Nodules** (helping to identify small, early-stage masses).
* **Pneumothorax** (making the subtle line of a collapsed lung more visible).

#### 3.2. Inverted + CLAHE: Highlighting Dense Structures

Conversely, applying CLAHE to the *inverted* image provides a different, powerful kind of enhancement. The inversion makes dense structures (originally white) become dark. The subsequent contrast enhancement on these now-dark areas can make subtle details within them more apparent to the human eye, which is often better at discerning detail in darker, sharper regions.

This method shows promise for identifying issues in high-density areas, such as:
* **Hairline Fractures** in bones, which might be missed in an overly bright image.
* **Vascular Calcifications**, by highlighting hardened arteries against the surrounding tissue.
* Identifying the precise borders of **dense masses or bone lesions**.

### 4. Conclusion

The main conclusion of this experiment is that **there is no single "best" enhancement method for all purposes**. The ideal pre-processing technique is context-dependent and should be chosen based on the diagnostic objective.

While **Standard CLAHE** proves superior for general soft tissue analysis, the **Inverted + CLAHE** method demonstrates significant potential as a specialized tool for highlighting features within bone and other dense structures.

Future work could involve quantitatively evaluating these methods by using them as a pre-processing step for a Machine Learning model trained to detect specific conditions (e.g., fractures vs. pneumonia) and measuring which method leads to higher diagnostic accuracy.