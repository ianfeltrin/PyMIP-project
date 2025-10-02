import numpy as np
import cv2
import matplotlib.pyplot as plt

caminho_da_imagem = 'data/raw/raio_x_chest.png'
imagem = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)

imagem_negativo = 255 - imagem

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('ORIGINAL')

plt.subplot(1, 2, 2)
plt.imshow(imagem_negativo, cmap='gray')
plt.title('INVERTIDO')

plt.show()