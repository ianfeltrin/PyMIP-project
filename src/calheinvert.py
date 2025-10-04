import cv2
import matplotlib.pyplot as plt

image_path = 'data/raw/raio_x_chest.png'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
inverted_image = 255 - original_image

#clahe
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
inverted_clahe = clahe.apply(inverted_image)
original_clahe = clahe.apply(original_image)

#histograns
histogram = cv2.calcHist([original_image], [0], None, [256], [0, 256])
inverted_histogram = cv2.calcHist([inverted_image], [0], None, [256], [0, 256])
clahe_histogram = cv2.calcHist([original_clahe], [0], None, [256], [0, 256])
inverted_clahe_histogram = cv2.calcHist([inverted_clahe], [0], None, [256], [0, 256])

#display
plt.figure(figsize=(12, 10))

#original_image subplot
plt.subplot(2, 4, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original image')

#inverted_image subplot
plt.subplot(2, 4, 2)
plt.imshow(inverted_image, cmap='gray')
plt.title('Inverted image')

#original_clahe subplot
plt.subplot(2, 4, 3)
plt.imshow(original_clahe, cmap='gray')
plt.title('Original image with Clahe')

#invertede_clahe subplot
plt.subplot(2, 4, 4)
plt.imshow(inverted_clahe, cmap='gray')
plt.title('Inverted image with Clahe')

#original_histogram
plt.subplot(2, 4, 5)
plt.plot(histogram)
plt.title('Original Histogram')

#inverted_hist
plt.subplot(2, 4, 6)
plt.plot(inverted_histogram)
plt.title('Inverted Histogram')

#original_clahe_histogram
plt.subplot(2, 4, 7)
plt.plot(clahe_histogram)
plt.title('Original clahe histogram')

#inverted_clahe_histogram
plt.subplot(2, 4, 8)
plt.plot(inverted_clahe_histogram)
plt.title('Inverted clahe Histogram')

plt.tight_layout()
plt.show()