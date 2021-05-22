import cv2
import numpy as np

x = np.uint8([250]) # pozitif int sayılar oluştur
y = np.uint8([10]) 

sonuc1 = x + y
print(sonuc1)
# 260 8 bitlik bir sayı olduğu için 260 % 2 mod alma işlemi yapıyor: 4 olur.

sonuc2 = cv2.add(x, y)
print(sonuc2) # 250 ile 10 toplayınca opencv de max değer: 255 olur

import cv2
import numpy as np

# 2 resmi belirli bir şeffaflık oranıyla toplama işlemi yani harmanlama
"""
1. parametre ilk resmim
2. bu remin yüzde olarak ne kadar kullanılacağı: %70
3. ikinci resmim
4. 2. resmim yüzde olarak ne kadar kullancağım: %30
5. ise gama değeri yani parlaklık
toplam = img1*0.7 + img2*0.3 + 0
"""
img1 = cv2.imread("cv2.png")
img2 = cv2.imread("r.jpg")

# ağırlıklı toplama işlemi yapıcaz
# 2 resmi birbirine şeffaf olarak ekledik.
toplam = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow("resim",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()