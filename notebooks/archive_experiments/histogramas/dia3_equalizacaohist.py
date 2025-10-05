import cv2
import matplotlib.pyplot as plt

caminho_da_imagem = 'data/raw/raio_x_chest.png'
image = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)
imagem_equalizada = cv2.equalizeHist(image)

histograma = cv2.calcHist([image], [0], None, [256], [0, 256])
equalizeHist = cv2.calcHist([imagem_equalizada], [0], None ,[256], [0, 256])

plt.figure(figsize=(15, 12))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')

plt.subplot(2, 2, 2)
plt.imshow(imagem_equalizada, cmap='gray')
plt.title('Imagem Equalizada')

plt.subplot(2, 2, 3)
plt.plot(histograma)
plt.title('Histograma original')

plt.subplot(2, 2, 4)
plt.plot(equalizeHist)
plt.title('Histograma equalizado')

plt.tight_layout()
plt.show()