# PyMIP: Investigando Overfitting no Treinamento de Redes Neurais com MNIST

*Author: Ian Feltrin*
*Date: 19 de Outubro de 2025*

---

### 1. Introdução: O Overfitting no Mundo Real vs. Fictício da IA

O *overfitting* representa um desafio fundamental no treinamento de modelos de Inteligência Artificial. Essencialmente, é a diferença crítica entre a IA compreender os padrões gerais aplicáveis ao **mundo real** versus memorizar as particularidades dos **dados de treinamento** (seu "mundo fictício"). Quando um modelo sofre overfitting, ele se torna tão especializado nos exemplos que viu durante o treino que perde a capacidade de generalizar para dados novos e inéditos, tornando-se ineficaz na prática. Este artigo documenta uma análise detalhada deste fenômeno, utilizando Deep Learning com o dataset MNIST como estudo de caso.

### 2. Metodologia: Treinamento Controlado e Análise de Convergência

Utilizou-se uma rede neural sequencial (Keras/TensorFlow) para classificar dígitos manuscritos (MNIST). O processo foi cuidadosamente desenhado:

#### 2.1. O Papel das Épocas (`Epochs`) no Treinamento
O treinamento foi controlado pelo número de **épocas** (`epochs`), onde cada época representa um ciclo completo de aprendizado sobre todo o conjunto de dados de treino. Quanto mais épocas, mais o modelo "estuda" e refina seus padrões internos. Contudo, como veremos, mais estudo nem sempre significa melhor aprendizado generalizado.

#### 2.2. Monitoramento Contínuo com Dados de Validação
Durante o `model.fit()`, **20% dos dados de treino foram separados** (`validation_split=0.2`) como um conjunto de validação. Isso permitiu monitorar, a cada época, não apenas a performance no material "conhecido" (treino), mas também em dados "novos" (validação), registrando `accuracy` (acurácia) e `loss` (erro).

#### 2.3. Análise da Taxa de Aprendizado (Delta Loss)
A velocidade do aprendizado foi quantificada calculando-se a variação (delta) da `loss` de treino entre épocas consecutivas: $\Delta L_n = L_{n} - L_{n-1}$. Uma diminuição progressiva nesse delta, tendendo a zero, indica que o modelo está convergindo para um platô de performance nos dados de treino.

#### 2.4. Avaliação Final: A Prova Cega no Conjunto de Teste
Após o treinamento (neste caso, por 20 épocas para forçar o fenômeno), o modelo foi avaliado (`model.evaluate()`) no conjunto de teste original do MNIST, garantindo uma medida final e imparcial de sua capacidade de generalização.

### 3. Resultados e Análise: A Divergência Revelada

#### 3.1. Convergência no Treino, Estagnação na Validação
A análise das métricas ao longo das 20 épocas revela o comportamento clássico do overfitting. Conforme visto nos gráficos abaixo (Figuras 1 e 2), a performance no conjunto de **treino** (linhas azuis) continua a melhorar, enquanto a performance no conjunto de **validação** (linhas vermelhas) atinge um platô e a **Loss de validação começa a subir**. Essa **divergência** é a assinatura visual do overfitting.

**Figura 1: Curvas de Loss (Erro) durante o Treinamento**
**Figura 2: Curvas de Acurácia durante o Treinamento**
![Curvas de Acurácia](https://github.com/ianfeltrin/PyMIP-project/blob/main/notebooks/project_03_overfitting_analysis/grafico_overfitting.png?raw=true)

#### 3.2. Performance Final: O Custo do Overfitting
A avaliação final no conjunto de teste quantifica o prejuízo da generalização causado pelo treinamento excessivo:

* **Acurácia de Treino (Final Epoch 20):** **~99.82%**
* **Acurácia de Teste (Após 20 Epochs):** **~97.77%**

A diferença substancial entre as duas acurácias confirma: o modelo se tornou um "especialista" nos dados de treino, mas perdeu parte de sua capacidade de lidar com a novidade.

### 4. Conclusão: O Mundo Fictício vs. O Mundo Real

Este experimento prático com o MNIST valida a importância crítica de monitorar o overfitting através das curvas de aprendizado, especialmente a `loss` de validação. O ponto onde a performance de validação estagna ou piora indica o momento ótimo para interromper o treinamento. Como observado: **_"quanto mais [a IA] aprende no mundo fictício, mais ela erra no mundo real."_**


# PyMIP: Investigating Overfitting in Neural Network Training with MNIST

*Author: Ian Feltrin*
*Date: October 19, 2025*

---

### 1. Introduction: Overfitting - AI's Real World vs. Fictional World

*Overfitting* is a critical challenge in training AI models. It distinguishes between an AI understanding general patterns applicable to the **real world** versus merely memorizing specifics from its **training data** (its "fictional world"). This article documents a detailed analysis of this phenomenon using Deep Learning with the MNIST dataset.

### 2. Methodology: Controlled Training and Convergence Analysis

A sequential neural network (Keras/TensorFlow) was used to classify MNIST digits. The process involved:

#### 2.1. The Role of Epochs in Training
Training was controlled by the number of **epochs**. More epochs allow the model to refine its patterns, but as shown, excessive training can harm generalization.

#### 2.2. Continuous Monitoring with Validation Data
Using `validation_split=0.2` during `model.fit()`, performance was monitored on both training and validation sets at each epoch, recording `accuracy` and `loss`.

#### 2.3. Learning Rate Analysis (Delta Loss)
The change (delta) in training `loss` between epochs ($\Delta L_n = L_{n} - L_{n-1}$) was analyzed to observe convergence, indicated by $\Delta L_n \to 0$.

#### 2.4. Final Evaluation: The Blind Test Set
After training (20 epochs), the model was evaluated (`model.evaluate()`) on the MNIST test set for an unbiased measure of generalization.

### 3. Results and Analysis: The Divergence Revealed

#### 3.1. Convergence vs. Divergence (Learning Curves)
The learning curves (Figures 1 and 2) show classic overfitting. While **training performance** (blue lines) keeps improving, **validation performance** (red lines) plateaus, and crucially, **validation loss starts to increase**. This **divergence** is the visual signature of overfitting.

**Figure 1: Loss Curves during Training**
**Figure 2: Accuracy Curves during Training**
![Accuracy Curves](https://github.com/ianfeltrin/PyMIP-project/blob/main/notebooks/project_03_overfitting_analysis/grafico_overfitting.png?raw=true)

#### 3.2. Final Performance: The Cost of Overfitting
The final test set evaluation quantifies the generalization gap:

* **Training Accuracy (End of Epoch 20):** **99.82%**
* **Test Accuracy (After 20 Epochs):** **97.77%**

The significant difference confirms overfitting: the model excelled on training data but struggled with novelty.

### 4. Conclusion: The Fictional World vs. The Real World

This experiment highlights the importance of monitoring validation metrics to detect overfitting. The point where validation performance degrades indicates the optimal stopping point. As noted: **_"the more [the AI] learns in the fictional world, the more it errs in the real world."_**