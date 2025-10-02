#IMPORTAR AS BIBLIOTECAS NECESSÁRIAS
import cv2
import matplotlib.pyplot as plt

#DEFINIR O CAMINHO DA IMAGEM
caminho_da_imagem = 'data/raw/WhatsApp Image 2025-07-15 at 21.31.37.jpg'

#LER A IMAGEM DO DISCO (cv2.imread) E (cv2.IMREAD_GRAYSCALE) JA GARANTE
#QUE A IMAGEM SERÁ LIDA EM TONS DE CINZA
image = cv2.imread(caminho_da_imagem)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#USAMOS O MATPLOTLIB PARA PREPARAR A IMAGEM PARA SER EXIBIDA NA TELA
#USAMOS O cmap='gray' PARA GARANTIR QUE SERÁ EM TONS DE CINZA
plt.imshow(rgb_image)

plt.title('Lolinha goldinha')
plt.xlabel('Gordura')
plt.ylabel('Fofura')

#MOSTRAR A JANELA NA TELA
plt.show()
