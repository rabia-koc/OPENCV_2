
import cv2

img = cv2.imread("1.jpeg")

print(img.shape)

# res = cv2.resize(img, (300, 300)) # yeniden boyutlandırma 

# küçültme işlemi yaptık
res = cv2.resize(img, None, fx = 0.5, fy = 0.5) # 2'sinede 1 yazarsak resim aynı kalır.

# küçültme büyültme işlemi yaptığımızda orjinallerdeki piksellere ne oluyor?
# büyültme yaptığımızda daha fazla piksel ekleniyor ve bu pikseller ortalama bulma işlemiyle ekleniyor.
# bunlar içinde matrixler kullanılıyor. matrisel çarpım işlemi yapılıyor. "interpolation ile"

res = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
# daha doğrusal bir sonuç veriyor.
# işlem gücü olarak biraz daha fazla zaman harcıyor.

cv2.imshow("img", img)
cv2.imshow("img", res)

cv2.waitKey()
cv2.destroyAllWindows()

