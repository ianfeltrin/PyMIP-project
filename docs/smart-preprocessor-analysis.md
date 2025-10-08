# PyMIP: Um Pré-Processador Inteligente para Redução de Ruído Adaptativa

*Author: Ian Feltrin*
*Date: 7 de Outubro de 2025*

---

### 1. Introdução: O Problema do Ruído em Imagens Médicas

Uma etapa fundamental em qualquer pipeline de processamento de imagens médicas é a redução de ruído, que pode ser gerado por sensores, transmissão ou mesmo pela própria técnica de aquisição da imagem. Contudo, o ruído não é uniforme. Diferentes tipos de ruído, como o **Gaussiano** (uma "estática" granulada) e o **Sal e Pimenta** (pixels pretos e brancos aleatórios), são combatidos de forma mais eficaz por filtros específicos (`GaussianBlur` vs. `MedianBlur`). A escolha manual de um filtro por um especialista é ineficiente, subjetiva e não escalável em um ambiente clínico de alto volume.

### 2. Metodologia

Para automatizar a escolha do filtro, foi desenvolvida a hipótese de que o **histograma** de uma imagem pode servir como uma "assinatura digital" para diagnosticar o tipo de ruído. A solução proposta foi construir um modelo de Machine Learning para classificar essa assinatura.

#### 2.1. Solução Proposta
Um classificador de Machine Learning foi proposto para analisar o histograma de uma imagem de entrada e predizer se ela contém ruído Gaussiano ou Sal e Pimenta, permitindo a aplicação automática do filtro de limpeza mais adequado.

#### 2.2. Criação do Dataset
Foi gerado um dataset sintético com 100 imagens de Raio-X: 50 corrompidas com ruído Gaussiano e 50 com ruído Sal e Pimenta.

#### 2.3. Extração de Features
Para cada imagem, o histograma de 256 bins foi calculado e normalizado para uma escala de 0 a 1. Este vetor de 256 pontos serviu como o vetor de *features* (as "pistas") para o modelo.

#### 2.4. Treinamento do Modelo
Um classificador SVM (Support Vector Machine) com kernel linear foi treinado utilizando 80% do dataset. Os 20% restantes foram reservados para um teste "cego" de validação.

### 3. Resultados e Análise

O modelo treinado, ao ser avaliado com o conjunto de teste de 20% (imagens que ele nunca havia visto), alcançou uma **acurácia de 100%**. Ele foi capaz de diferenciar perfeitamente entre os dois tipos de ruído com base apenas em seus histogramas, provando a validade da hipótese.

### 4. Conclusão e Próximos Passos

Este experimento comprova que a análise de histogramas é uma abordagem viável e altamente eficaz para a classificação automática de tipos de ruído em imagens, validando o conceito do "Pré-processador Inteligente".

**Próximos Passos:**
* Expandir o dataset para incluir mais tipos de ruído e também imagens limpas.
* Integrar este classificador ao "Otimizador de Análise de Fraturas", para que ele limpe a imagem automaticamente antes de gerar as visões de análise.
* Explorar o uso de Redes Neurais (Deep Learning) para esta mesma tarefa e comparar a performance.


# PyMIP Project: An Intelligent Pre-processor for Adaptive Noise Reduction

*Author: Ian Feltrin*
*Date: October 7, 2025*

---

### 1. Introduction: The Problem of Noise in Medical Imaging

A fundamental step in any medical image processing pipeline is noise reduction. However, noise is not uniform; different sources (e.g., sensors, transmission) generate various artifacts. Two common forms are:

* **Gaussian Noise:** A "static-like" grain that affects all pixels.
* **Salt & Pepper Noise:** Random black (0) and white (255) pixels appearing on the image.

Each noise type is best countered by a specific filter (`GaussianBlur` for Gaussian, `MedianBlur` for Salt & Pepper). Manually selecting a filter is inefficient, subjective, and not scalable in a high-volume clinical environment.

### 2. Methodology

To automate the filter selection process, the hypothesis was that an image's **histogram** could serve as a "digital signature" to diagnose the noise type. The proposed solution was to build a Machine Learning model to classify this signature.

#### 2.1. Proposed Solution
An ML classifier was proposed to analyze an input image's histogram and predict whether it contains Gaussian or Salt & Pepper noise, enabling the automatic application of the optimal cleaning filter.

#### 2.2. Dataset Creation
A synthetic dataset of 100 X-ray images was generated: 50 corrupted with Gaussian noise and 50 with Salt & Pepper noise.

#### 2.3. Feature Extraction
For each image, its 256-bin histogram was calculated and normalized to a 0-1 scale. This 256-point vector served as the feature vector (the "clues") for the model.

#### 2.4. Model Training
A Support Vector Machine (SVM) classifier with a linear kernel was trained using 80% of the dataset. The remaining 20% was held out for a blind validation test.

### 3. Results and Analysis

The trained model, when evaluated on the 20% test set, achieved an **accuracy of 100%**. It was able to perfectly differentiate between the two noise types based solely on their histogram signatures, proving the hypothesis to be valid.

### 4. Conclusion and Future Work

This experiment proves that histogram analysis is a viable and highly effective approach for the automatic classification of noise types. The 100% accuracy validates the "Intelligent Pre-processor" concept.

**Future Work:**
* Expand the dataset to include more noise types and also clean images.
* Integrate this classifier into the "Fracture Analysis Optimizer" to automatically denoise images before generating analysis views.
* Explore the use of Neural Networks (Deep Learning) for this same task and compare performance.