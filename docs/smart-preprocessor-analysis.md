# PyMIP: Um Pré-Processador Inteligente para Redução de Ruído Adaptativa

*Author: Ian Feltrin*
*Date: 7 de Outubro de 2025*

---

### 1. Introdução: O Problema do Ruído em Imagens Médicas

Imagens médicas digitais são suscetíveis a diferentes tipos de ruído, que podem comprometer a análise visual e automática. A escolha de um filtro de limpeza adequado é crucial, pois um filtro otimizado para um tipo de ruído pode ser ineficaz em outro. Este projeto explora uma solução de Machine Learning para automatizar essa escolha.

![Comparativo dos Tipos de Ruído](https://github.com/ianfeltrin/PyMIP-project/blob/main/data/processed/filters.png?raw=true)

### 2. Metodologia e Análise Forense

A hipótese central é que o **histograma** de uma imagem serve como uma "assinatura digital" para diagnosticar o tipo de ruído. Para provar isso, foi construído um classificador SVM (Support Vector Machine) treinado para reconhecer essas assinaturas.

#### 2.1. Extração de Features: A Assinatura do Histograma

**Assinatura do Ruído Gaussiano:**
Este ruído tende a "achatar e alargar" o histograma original. Os picos se tornam mais baixos e as curvas mais suaves, como se o gráfico tivesse sido "borrado".

![Histograma do Ruído Gaussiano](https://github.com/ianfeltrin/PyMIP-project/blob/main/data/processed/hist_gaussian.png?raw=true)

**Assinatura do Ruído Sal e Pimenta:**
Este ruído cria pixels nos valores extremos. Sua assinatura no histograma é inconfundível: dois picos agudos e isolados exatamente nos valores 0 (pimenta/preto) e 255 (sal/branco).

![Histograma do Ruído Sal e Pimenta](https://github.com/ianfeltrin/PyMIP-project/blob/main/data/processed/hist_s&p.png?raw=true)

#### 2.2. Validação da Escolha do Filtro

Com as assinaturas identificadas, testamos a eficácia do filtro correto para cada caso. O `GaussianBlur` se mostrou ideal para o ruído Gaussiano, enquanto o `MedianBlur` foi superior para o Sal e Pimenta.

![Validação dos Filtros de Limpeza](https://github.com/ianfeltrin/PyMIP-project/blob/main/data/processed/clean_images.png?raw=true)

#### 2.3. Treinamento do Modelo SVM
Com a prova de que cada ruído tem uma assinatura e um remédio específico, um classificador SVM foi treinado com os 100 histogramas (vetores de 256 posições) como dados de entrada e os rótulos "Gaussiano" (0) ou "Sal e Pimenta" (1) como gabarito.

---
### 3. Resultados: Um Classificador com 100% de Acurácia

O modelo, treinado com 80% dos dados, foi validado com os 20% restantes e alcançou uma **acurácia de 100%**, provando ser capaz de diagnosticar o tipo de ruído com perfeição.

![Fluxograma da Solução](https://github.com/ianfeltrin/PyMIP-project/blob/main/data/raw/fluxogram.png?raw=true)

---
### 4. Conclusão

Este experimento valida com sucesso o conceito do "Pré-processador Inteligente". Demonstra-se que é possível treinar um modelo de Machine Learning para, de forma autônoma, identificar diferentes tipos de ruído e permitir a aplicação do filtro mais eficaz, um passo fundamental para a criação de pipelines de processamento de imagens mais robustos.

# PyMIP Project: An Intelligent Pre-processor for Adaptive Noise Reduction

*Author: Ian Feltrin*
*Date: October 7, 2025*

---

### 1. Introduction: The Problem of Noise in Medical Imaging

A fundamental step in any medical image processing pipeline is noise reduction. However, noise is not uniform; different sources generate various artifacts. This project explores a Machine Learning solution to automate the selection of the appropriate filter for a given noise type.

![Noise Type Comparison](https://github.com/ianfeltrin/PyMIP-project/blob/main/data/processed/filters.png?raw=true)

### 2. Methodology

To automate the filter selection, the hypothesis was that an image's **histogram** could serve as a "digital signature" for its noise type. An SVM classifier was trained to recognize these signatures.

#### 2.1. Feature Extraction: The Histogram Signature

**Gaussian Noise Signature:** This noise type tends to "flatten and widen" the original histogram, creating a smoother, more spread-out distribution.

![Gaussian Noise Histogram](https://github.com/ianfeltrin/PyMIP-project/blob/main/data/processed/hist_gaussian.png?raw=true)

**Salt & Pepper Noise Signature:** This noise creates pixels at extreme values. Its histogram signature is unmistakable: two sharp, isolated **spikes** at the 0 (pepper/black) and 255 (salt/white) bins.

![Salt_and_Pepper_Noise_Histogram](https://github.com/ianfeltrin/PyMIP-project/blob/main/data/processed/hist_s&p.png?raw=true)

#### 2.2. Filter Choice Validation
With the signatures identified, tests confirmed that `GaussianBlur` is ideal for Gaussian noise, while `MedianBlur` is superior for Salt & Pepper noise.

![Filter Validation Results](https://github.com/ianfeltrin/PyMIP-project/blob/main/data/processed/clean_images.png?raw=true)

#### 2.3. SVM Model Training
An SVM classifier was trained on a synthetic dataset of 100 images. The model used the 256-bin histograms as input features and the noise types ("Gaussian" or "S&P") as labels. The data was split 80/20 for training and testing.

---
### 3. Results and Analysis

The trained model, when evaluated on the 20% test set, achieved an **accuracy of 100%**. It was able to perfectly differentiate between the two noise types based solely on their histogram signatures.

---
### 4. Conclusion and Future Work

This experiment successfully validates the "Intelligent Pre-processor" concept. It demonstrates that an ML model can autonomously identify noise types and enable the application of the most effective filter.

**Future Work:**
* Expand the dataset to include more noise types.
* Integrate this classifier into the "Fracture Analysis Optimizer".
* Explore the use of Deep Learning for this same task.