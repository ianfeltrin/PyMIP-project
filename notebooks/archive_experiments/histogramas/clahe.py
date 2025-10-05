#O clahe consiste em melhorar o histograma equalizado.
#O clahe cria diversas janelas e equaliza cada uma para uma melhor visualização

import cv2
import matplotlib.pyplot as plt

caminhodaimagem = './data/raw/raio_x_chest.png'
imagem = cv2.imread(caminhodaimagem, cv2.IMREAD_GRAYSCALE)
imagemEqualizada = cv2.equalizeHist(imagem)

#MÉTODO CLAHE
#1 criamos um objeto CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#Cliplimit = 2,0 define o limite de contraste para não gerar muito ruído
#TileGridSize define o tamanho da janela, 8x8 pixels nesse caso

#2 agora aplicamos o clahe na imagem original
imagem_clahe = clahe.apply(imagem)

#histogramas
hist = cv2.calcHist([imagem], [0], None, [256], [0, 256])
equahist = cv2.calcHist([imagemEqualizada], [0], None, [256], [0, 256])
clahehist = cv2.calcHist([imagem_clahe], [0], None, [256], [0, 256])

plt.figure(figsize=(20, 15))

plt.subplot(3, 3, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Original')

plt.subplot(3, 3, 2)
plt.imshow(imagemEqualizada, cmap='gray')
plt.title('Imagem equalizada')

plt.subplot(3, 3, 3)
plt.imshow(imagem_clahe, cmap='gray')
plt.title('Imagem equalizada com CLAHE')

plt.subplot(3, 3, 7)
plt.plot(hist)
plt.title('Histograma original')

plt.subplot(3, 3, 8)
plt.plot(equahist)
plt.title('Histograma Equalizado')

plt.subplot(3, 3, 9)
plt.plot(clahehist)
plt.title('Histograma equal. CLAHE')

plt.tight_layout()
plt.show()