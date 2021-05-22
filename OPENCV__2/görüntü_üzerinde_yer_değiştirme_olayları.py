
import cv2
import numpy as np

img = cv2.imread("1.jpeg")

print(img.shape)

rows, cols = img.shape[:2] # 2'ye kadar aldık çünkü resmin kanalları 3 boyutlu

translation_matrix = np.float32([
    [1, 0, 50], # 50 yerlerine 25 yazarsak tam pencereye resim ortalanmış olur
    [0, 1, 50]])

# çarpma işlemi yani görüntü üzerinde gezme işlevi ise 
img_translation = cv2.warpAffine(img, translation_matrix, (cols + 50, rows + 50))
# 3. parametreye yer değiştirilme işlemi yapıldıktan sonra elde edilecek görüntüdeki boyutları gerekiyor.
# biz bunu orjinal görüntünün boyutlarıyla eşleştiricez.

cv2.imshow("img", img)
cv2.imshow("img_translation", img_translation) 
# boyutları aynı kalarak 50 piksel sağa  ve 50 piksel aşağı gitti.
# eğer cols+50, rows+50 yazarsak kırpılmadan yerleştirilir.

cv2.waitKey()
cv2.destroyAllWindows()


