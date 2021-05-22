
# * ***ÇERÇEVE EKLEME İŞLEMİ***

import cv2
from matplotlib import pyplot as plt
import numpy as np

BLUE = [255, 0, 0]

img1 = cv2.imread('cv2.png')

# cv2.copyMakeBorder() açıklaması:
# ilk parametre resim
# 2, 3, 4, 5 kaçar pikselden oluştuğunu yazdım
# 6. ise çerçeve türü

replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = BLUE)

plt.subplot(231)
plt.imshow(img1, 'gray')
plt.title('ORIGINAL')
plt.subplot(232)
plt.imshow(replicate, 'gray')
plt.title('REPLICATE')
plt.subplot(233)
plt.imshow(reflect, 'gray')
plt.title('REFLECT')
plt.subplot(234)
plt.imshow(reflect101, 'gray')
plt.title('REFLECT_101')
plt.subplot(235)
plt.imshow(wrap, 'gray')
plt.title('WRAP')
plt.subplot(236)
plt.imshow(constant, 'gray')
plt.title('CONSTANT')

plt.show()

"""
çerçeve erklerken BLUE = [255, 0, 0] yazdık.
ama çerçeve oluştuğunda kırmızı renkte gözüküyordu neden?
-- 
Çünkü OpenCV BGR formatını kullanırken Matplotlib RGB formatını kullanıyor 
ve biz mavi olarak belirttik ama 
plt.imshow ile gösterirken maviler kırmızı, kırmızılar mavi olarak gösterildi."""