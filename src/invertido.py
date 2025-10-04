import numpy as np
import cv2
import matplotlib.pyplot as plt

caminho_da_imagem = 'data/raw/raio_x_chest.png'
imagem = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)

imagem_negativo = 255 - imagem

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
imagem_clahe = clahe.apply(imagem_negativo)

plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(imagem, cmap='gray')
plt.title('ORIGINAL')

plt.subplot(1, 3, 2)
plt.imshow(imagem_negativo, cmap='gray')
plt.title('INVERTIDO')

plt.subplot(1, 3, 3)
plt.imshow(imagem_clahe, cmap='gray')
plt.title('TESTE')

plt.tight_layout()
plt.show()