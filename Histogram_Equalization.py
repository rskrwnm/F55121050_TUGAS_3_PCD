import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menampilkan histogram citra
def plot_histogram(image, title):
    plt.hist(image.ravel(),256,[0,256])
    plt.title(title)
    plt.show()

# Membaca citra-citra dengan empat tipe yang berbeda
img_dark = cv2.imread('dark.png', cv2.IMREAD_GRAYSCALE)
img_bright = cv2.imread('bright.png', cv2.IMREAD_GRAYSCALE)
img_low = cv2.imread('low_contrast.png', cv2.IMREAD_GRAYSCALE)
img_high = cv2.imread('high_contrast.png', cv2.IMREAD_GRAYSCALE)

# Melakukan histogram equalization pada setiap citra
img_dark_eq = cv2.equalizeHist(img_dark)
img_bright_eq = cv2.equalizeHist(img_bright)
img_low_eq = cv2.equalizeHist(img_low)
img_high_eq = cv2.equalizeHist(img_high)

# Menampilkan citra asli, histogram asli, hasil histogram equalization, dan histogram hasil equalization
plot_histogram(img_dark, 'Histogram Citra Gelap')
cv2.imshow('Citra Gelap', img_dark)
plot_histogram(img_dark_eq, 'Histogram Hasil Histogram Equalization Citra Gelap')
cv2.imshow('Hasil Histogram Equalization Citra Gelap', img_dark_eq)

plot_histogram(img_bright, 'Histogram Citra Terang')
cv2.imshow('Citra Terang', img_bright)
plot_histogram(img_bright_eq, 'Histogram Hasil Histogram Equalization Citra Terang')
cv2.imshow('Hasil Histogram Equalization Citra Terang', img_bright_eq)

plot_histogram(img_low, 'Histogram Citra Kekontrasan Rendah')
cv2.imshow('Citra Kekontrasan Rendah', img_low)
plot_histogram(img_low_eq, 'Histogram Hasil Histogram Equalization Citra Kekontrasan Rendah')
cv2.imshow('Hasil Histogram Equalization Citra Kekontrasan Rendah', img_low_eq)

plot_histogram(img_high, 'Histogram Citra Kekontrasan Tinggi')
cv2.imshow('Citra Kekontrasan Tinggi', img_high)
plot_histogram(img_high_eq, 'Histogram Hasil Histogram Equalization Citra Kekontrasan Tinggi')
cv2.imshow('Hasil Histogram Equalization Citra Kekontrasan Tinggi', img_high_eq)

cv2.waitKey(0)
cv2.destroyAllWindows()
