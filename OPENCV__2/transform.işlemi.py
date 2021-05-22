# 3 tane nokta seçicem
# bu 3 nokta yeni oluşacak resimde hangi noktalara gelmiş olacağını vermiş olacağım
# böylece burda bir transformation işlemi olacak.

import cv2
import numpy as np

img = cv2.imread("1.jpeg")

rows, cols = img.shape[:2]

print(rows)

src_points = np.float32([
    [0, 0],
    [cols -1, 0], 
    [0, rows -1]])
# 2. nokta en sağ üst. neden -1 aldık? çünkü rows=512 eşit ama 511 dahil en son
# 3. nokta ise en alttaki  soldaki nokta

# şimdi yeni oluşacak resimde hangi noktalara geleceğini seçmem gerekiyor.
dst_points = np.float32([
    [0, 0],
    [int(0.6 * (cols -1)), 0],
    [int(0.4 * (cols -1)), rows -1]])
# 2. yi %60 sol tarafa aldı (481*0.6)=288. piksele denk gelir. col=481'dir
# 3. de x'i %40 sağa kaydırdı.

affine_matrix = cv2.getAffineTransform(src_points, dst_points) # ilki giriş, 2.si çıkış 

# resimle çarpma işlemi
img_output = cv2.warpAffine(img, affine_matrix, (cols, rows))

cv2.imshow("img", img)
cv2.imshow("img_output", img_output)

cv2.waitKey()
cv2.destroyAllWindows()



