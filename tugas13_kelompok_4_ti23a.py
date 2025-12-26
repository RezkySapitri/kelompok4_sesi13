# =============================================
# Tugas Sesi 13 – Image Security (XOR Encryption)
# Study Kasus : Citra Medis X-Ray
# Kelompok 4 - TI23A
# =============================================

import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# 1. Load Citra (file harus berada satu folder dengan script)
# ---------------------------------------------
img = cv2.imread('x-ray.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("❌ Gambar x-ray.png tidak ditemukan! Pastikan file ada di folder yang sama.")

print("✔️ Citra berhasil dimuat")

# ---------------------------------------------
# 2. Preprocessing — Noise Reduction & Contrast Equalization
# ---------------------------------------------
img_blur = cv2.GaussianBlur(img, (3,3), 0)
img_preprocessed = cv2.equalizeHist(img_blur)

# simpan untuk pembanding dekripsi
preprocessed_for_compare = img_preprocessed.copy()

print("✔️ Preprocessing selesai")

# ---------------------------------------------
# 3. Enkripsi XOR
# ---------------------------------------------
key = 170
encrypted_img = np.bitwise_xor(img_preprocessed, key)

# simpan hasil enkripsi
cv2.imwrite('xray_encrypted.png', encrypted_img)
print("✔️ Citra terenkripsi disimpan sebagai: xray_encrypted.png")

# ---------------------------------------------
# 4. Dekripsi XOR
# ---------------------------------------------
decrypted_img = np.bitwise_xor(encrypted_img, key)
print("✔️ Dekripsi selesai")

# ---------------------------------------------
# 5. Validasi Dekripsi
# ---------------------------------------------
if np.array_equal(preprocessed_for_compare, decrypted_img):
    print("🟢 Dekripsi berhasil: Citra kembali sama setelah preprocessing")
else:
    print("🔴 Dekripsi gagal: Citra tidak sama")

# ---------------------------------------------
# 6. Visualisasi Hasil
# ---------------------------------------------
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Citra Asli (X-Ray)')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(encrypted_img, cmap='gray')
plt.title('Citra Terenkripsi (XOR)')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(decrypted_img, cmap='gray')
plt.title('Citra Setelah Dekripsi')
plt.axis('off')

plt.show()
