import cv2
import matplotlib.pyplot as plt

caminho_da_imagem = 'data/raw/raio_x_chest.png'
image = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)

# --- CÁLCULO DO HISTOGRAMA ---

# A função calcHist do OpenCV calcula o histograma.
# [imagem]: a imagem que queremos analisar (precisa estar em uma lista).
# [0]: o canal da cor (0 para tons de cinza).
# None: uma máscara, que não vamos usar agora.
# [256]: o número de "barrinhas" no nosso gráfico (uma para cada tom, de 0 a 255).
# [0, 256]: a faixa de valores dos pixels (de 0 a 255).
histograma = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 5))

#Imagem original
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')

plt.subplot(1, 2, 2)
plt.plot(histograma)
plt.title('Histograma')
plt.xlabel('Tons de cinza (0 = Preto, 256 = Branco)')
plt.ylabel('Quantidade de pixels')
plt.xlim([0, 256])

plt.show()