
import cv2
import numpy as np

img = cv2.imread("1.jpeg")

rows, cols = img.shape[:2]

# resmi döndürmek için bir matrixe ihtiyacım var.

rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 0.7)
# içine merkezlerini yazdık. 0.7 yazarsak %30'luk küçültme işlemi olucak ama tam ekrana girecek
# 30 derece döndüreceğimi yazdım.
# son parametreyi küçültme ve büyültme olarak kullanıyoruz.

# tekrar resim üzerine çaprma işlemi yapmak için 
img_rotation =cv2.warpAffine(img, rotation_matrix, (cols, rows))
# şu kısım sonuçta oluşan resmin bilgilerini içeriyor.

cv2.imshow("img", img)
cv2.imshow("img_rotation", img_rotation)

cv2.waitKey()
cv2.destroyAllWindows()
