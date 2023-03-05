import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan histogram citra
def plot_histogram(image, title):
    plt.hist(image.ravel(),256,[0,256])
    plt.title(title)
    plt.show()
# Membaca empat citra
img_dark = cv2.imread('dark.png', cv2.IMREAD_GRAYSCALE)
img_bright = cv2.imread('bright.png', cv2.IMREAD_GRAYSCALE)
img_low_contrast = cv2.imread('low_contrast.png', cv2.IMREAD_GRAYSCALE)
img_high_contrast = cv2.imread('high_contrast.png', cv2.IMREAD_GRAYSCALE)

# Menampilkan empat citra dan histogram masing-masing citra
plot_histogram(img_dark, 'Histogram Citra Gelap')
cv2.imshow('Citra Gelap', img_dark)

plot_histogram(img_bright, 'Histogram Citra Terang')
cv2.imshow('Citra Terang', img_bright)

plot_histogram(img_low_contrast, 'Histogram Citra Kekontrasan Rendah')
cv2.imshow('Citra Kekontrasan Rendah', img_low_contrast)

plot_histogram(img_high_contrast, 'Histogram Citra Kekontrasan Tinggi')
cv2.imshow('Citra Kekontrasan Tinggi', img_high_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()