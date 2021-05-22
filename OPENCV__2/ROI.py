# ROI = REGİON OF IMAGE

# bir resmin belirli bir alanının kırpılması işlemi ve oradan ayrı bir pencereye ayrılması ya da başka bir yere yerleştirilmesi gibi
# bu işlem ile önce yüz tespiti yapıp sonra yüz üzerinde göz aramak aynı zamanda doğruluğu da arttırır.

import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("r.jpg")

kirp = resim[500:800, 500:800]  # resmi kırpma işlemi yapıcaz

# kırptığım görüntüyü orjinal resim üzerine yerleştirme
resim[100:400, 1400:1700] = kirp  # sağ tarfatakini solun içine göndermiş olduk.

plt.subplot(121)
plt.imshow(resim)
plt.subplot(122)
plt.imshow(kirp)
plt.show()
