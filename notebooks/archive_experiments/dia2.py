import cv2
import numpy as np
import matplotlib.pyplot as plt

caminho_da_imagem = 'data/raw/raio_x_chest.png'
imagem = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)

imagem_mais_brilhante = cv2.add(imagem, 50)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('ORIGINAL')

plt.subplot(1, 2, 2)
plt.imshow(imagem_mais_brilhante, cmap='gray')
plt.title('MAIS BRILHANTE (+50 PIXELS)')

plt.show()