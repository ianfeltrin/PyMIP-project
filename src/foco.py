import cv2
import numpy as np
import matplotlib.pyplot as plt

caminho_da_imagem = 'data/raw/hand_xray.jpeg'
imagem = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)
imagemf = imagem.copy()
imagem_cortada = imagem[50:300, 130:230]
imagem_clara = cv2.add(imagem_cortada, 70)
imagemf[50:300, 130:230] = imagem_clara

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap='gray')

plt.subplot(1, 2, 2)
plt.imshow(imagemf, cmap='gray')

plt.show()
