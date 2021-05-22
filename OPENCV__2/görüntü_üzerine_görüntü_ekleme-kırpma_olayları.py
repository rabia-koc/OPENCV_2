import cv2
import numpy as np

# bitsel olarak çarpma işlemi yapıcaz 
# amacımız cv2.png resmini r.jpg'ye eklemek

img1 = cv2.imread("cv2.png")
img2 = cv2.imread("r.jpg")

x,y,z = img1.shape # img1.shape=(369,300,3), img2.shape=(1080, 1920, 3)
roi = img2[0:x,0:y] # img2'nin içinden bir kırpma işlemi
# yani 2.resmimden 1.resmimim alanı kadar kırpma yapıyorum

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) # renk uzayını değiştirmek için 

ret, mask = cv2.threshold(img1_gray, 10, 255, cv2.THRESH_BINARY)  # (3.resim)
# eşikleme işlemi yapıyoruz
# 10 pikselin üzerindekileri alıp beyaz yapıyor geri kalanlar siyah

"""
kırptığımızda yerde bitsel olarak çarpma işlemi yapıcaz.
yani görüntünün eklemek istediğim kısımları 0 diğer kısımlar aynı renk kalsın.
"""
"""
anagörüntüde arka planın anagörüntünün rengini istiyor isem 1 olması lazım ki anagörüntüyle 
çarptığım zaman anagörüntünün arka plan rengini alabileyim
tersleme işlemi yapıcaz 0'lar 1, 1'ler 0
"""

mask_inv = cv2.bitwise_not(mask) # tersleme (4.resim)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  #(5.resim)

# iki tane roi ile çarptık çünkü 2 tane aynı şeyi çarptığımızda sonuç aynı ifade olur.
# sonra diğer görseli bunun üzerine ekleme işlemi
# mask 0 ile 1'lerden oluşan bir resim
# 0'lar siyah olarak maskem oluyor, arka planda kalan beyazlar ise 
# ana resimdeki asıl renkli kısımla çarpıldığında aynı renge tekabül ettiği için 
# sadece logoya ekleyceğim kısmı siyahlaştırmış oluyorum

# renkli kısımları almak için
img2_fg = cv2.bitwise_and(img1, img1, mask=mask) # opencv resminin ilk hali

toplam = cv2.add(img1_bg,img2_fg)  # (6.resim)

img2[0:x,0:y] = toplam  # (7.resim)

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
cv2.imshow("resim",img2)
cv2.imshow("resim2",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()


