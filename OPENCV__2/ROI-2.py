# tek kanallı bir resim oluştu siyah ve beyaz
# tek renk uzayına sahip

import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("r.jpg", 0)

kirp = resim[500:800, 500:800]

resim[100:400, 1400:1700] = kirp

plt.subplot(121)
plt.imshow(resim, "gray")
plt.subplot(122)
plt.imshow(kirp, "gray")
plt.show()