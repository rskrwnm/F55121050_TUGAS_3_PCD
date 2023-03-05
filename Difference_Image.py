import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load dua citra
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')

# Konversi citra menjadi grayscale
grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Menghitung difference image
diffImg = cv2.absdiff(grayImg1, grayImg2)

# Menampilkan citra dan difference image
plt.subplot(1, 3, 1)
plt.imshow(grayImg1, cmap='gray')
plt.title('Citra 1')
plt.subplot(1, 3, 2)
plt.imshow(grayImg2, cmap='gray')
plt.title('Citra 2')
plt.subplot(1, 3, 3)
plt.imshow(diffImg, cmap='gray')
plt.title('Difference Image')
plt.show()
