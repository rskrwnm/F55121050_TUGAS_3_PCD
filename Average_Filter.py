import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load citra
img = cv2.imread('img1.jpg')

# Konversi citra menjadi grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Kernel untuk average filter
kernel = np.ones((5,5), np.float32)/25

# Melakukan operasi average filter
avgImg = cv2.filter2D(grayImg, -1, kernel)

# Menampilkan citra asli dan citra hasil average filter
plt.subplot(1,2,1)
plt.imshow(grayImg, cmap='gray')
plt.title('Citra Asli')
plt.subplot(1,2,2)
plt.imshow(avgImg, cmap='gray')
plt.title('Citra Hasil Average Filter')
plt.show()




