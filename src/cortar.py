import cv2
import matplotlib.pyplot as plt

caminho_da_imagem = 'data/raw/raio_x_chest.png'
imagem = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)

imagem_cortada = imagem[500:2000, 500:1500]
imagem_cortada_menosbrilho = cv2.subtract(imagem_cortada, 50)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('ORIGINAL')

plt.subplot(1, 2, 2)
plt.imshow(imagem_cortada_menosbrilho, cmap='gray')
plt.title('TENTATIVA')

plt.show()