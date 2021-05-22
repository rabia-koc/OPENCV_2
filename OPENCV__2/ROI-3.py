# bu 3 tane renk uzayını tek tek elde edebilir miyim?

import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("r.jpg")

b, g, r = cv2.split(resim) # tek tek renk uzaylarına ayırdı

resim2 = cv2.merge((b, g, r)) # işlem yaptıktan sonra resim2 olarak birleştirdi.

# daha hızlı yapmak için
# b = resim[:, :, 0] # tüm x ve y piksellerini al ve 0. kanalını al

resim[:, :, 2] = 0 # kırmızıları sildik

cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()