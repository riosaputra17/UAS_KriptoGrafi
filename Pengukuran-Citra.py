import cv2
import numpy as np
import matplotlib.pyplot as plt


def calculate_mse(image1, image2):
    return np.mean((image1 - image2) ** 2)


def calculate_psnr(mse, max_pixel):
    return 20 * np.log10(max_pixel / np.sqrt(mse))


# Citra pertama dan kedua (pastikan ukurannya sama)
image1 = cv2.imread("ktm.jpg")  # Masukkan nama file citra pertama di sini
image2 = cv2.imread("sizuki.png")  # Masukkan nama file citra kedua di sini

# Konversi citra ke grayscale jika perlu
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Inisialisasi daftar untuk menyimpan nilai MSE dan nilai x (indeks)
mse_values = []
x_values = []

# Iterasi untuk menghasilkan rentang nilai x dari 0 hingga 256
for i in range(257):
    # Hitung nilai MSE untuk setiap x
    mse = calculate_mse(image1_gray.astype(float), (image2_gray + i) % 256)
    mse_values.append(mse)
    x_values.append(i)
    # Hitung Peak Signal-to-Noise Ratio (PSNR)
max_pixel = 255.0  # Piksel maksimum untuk citra 8-bit grayscale
psnr = calculate_psnr(mse, max_pixel)

print(f"Nilai MSE: {mse}")
print(f"Nilai PSNR: {psnr} dB")

# Plot grafik garis MSE
# plt.figure(figsize=(8, 6))
# plt.plot(x_values, mse_values, color='blue')
# plt.xlabel('Perubahan Intensitas Piksel')
# plt.ylabel('MSE')
# plt.title('Grafik MSE terhadap Perubahan Intensitas Piksel')
# plt.grid(True)
# plt.show()
