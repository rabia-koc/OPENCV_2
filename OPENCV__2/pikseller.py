import cv2

resim = cv2.imread("r.jpg")
# yüklediğimiz resmin pikseline ulaşabiliyor muyuz ?

px = resim[100, 100]  # x ve y deki koordinatlar olarak düşün
print(px)

# buradaki 3 değer bunun renkli bir görüntü olduğunu söyler.
# bgr formatında okunuyor yani mavi yeşil kırmızı olarak sayı kodları o renkleri temsil ediyor.
# bu değerler 0 ile 255 arasında değişiyor.
# 0: siyah 255: beyaz

# her bir kanala ulaşabilirim ve değerini değiştirebilirim.

px_blue = resim[100, 100, 0]  # yani 0. kanal: 146
print(px_blue)

resim[100, 100, 0] = 255
px_blue = resim[100, 100, 0]
print(px_blue)

# tüm değerleri değiştirme 
resim[100, 100] = [255, 255, 255]
print(resim[100, 100])

# numpy ile bu işlemi daha hızlı yapabilirz.

import numpy as np

print(resim.item(100, 100, 0)) # hangi kanal olduğunu yazmak zorundayız.

resim.itemset((100, 100, 0), 100)  # kanal değiştirmek için
# 0. kanalı 100 ile değiştik
print(resim[100, 100])

# resmin genel özelliklerine ulaşmak için
print(resim.shape) # boyutu

print(resim.size)  # boyutu

print(resim.dtype)



