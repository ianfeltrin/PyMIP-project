import cv2
import matplotlib.pyplot as plt

caminho_da_imagem = 'data/raw/raio_x_chest.png'

imagem = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)

plt.imshow(imagem, cmap='gray')
plt.show()