import cv2
import numpy as np

caminho_da_imagem = 'data/raw/hand_xray.jpeg'

# Carregamos a imagem em tons de cinza, como sempre
imagem = cv2.imread(caminho_da_imagem, cv2.IMREAD_GRAYSCALE)

# --- A INVESTIGAÇÃO FORENSE COMEÇA AQUI ---
print("--- INICIANDO RELATÓRIO DA AUTÓPSIA ---")

# Checagem 1: Qual o tipo de dado? (Nossa expectativa é 'uint8')
print(f"Tipo de dado (dtype): {imagem.dtype}")

# Checagem 2: Qual o valor do pixel mais escuro? (Esperamos algo perto de 0)
print(f"Valor mínimo do pixel: {imagem.min()}")

# Checagem 3: Qual o valor do pixel mais claro? (Esperamos algo perto de 255)
print(f"Valor máximo do pixel: {imagem.max()}")

print("--- FIM DO RELATÓRIO ---")