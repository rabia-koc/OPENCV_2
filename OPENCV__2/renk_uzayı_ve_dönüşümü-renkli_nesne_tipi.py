
# * ***görüntüleri bir renk uzayından diğerine, örneğin BGR <-> Gray, BGR <-> HSV v. dönüştürmeyi görücez.***
# * ***Renkli nesne tespiti***
# * ***Renk Uzayları nedir?***
# * ***cv2.inRange()***

import cv2
import numpy as np

"""
for i in dir(cv2):
    if "COLOR_" in i:
        print(i)"""

camera = cv2.VideoCapture(0) # kameradan görüntü alacğım için kamera belirledim.

def nothing(x):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("H1", "frame", 0, 359, nothing) #renk değiştirmek için
cv2.createTrackbar("H2", "frame", 0, 359, nothing)
cv2.createTrackbar("S1", "frame", 0, 255, nothing)
cv2.createTrackbar("S2", "frame", 0, 255, nothing)
cv2.createTrackbar("V1", "frame", 0, 255, nothing)
cv2.createTrackbar("V2", "frame", 0, 255, nothing)
# 1.si ismi
# 2.si hangi pencerede olacağı
# 3., 4. 0 ile 359 değerleri arasında
# 4.sü fonk. ismi

# ret değişkenini kullanmıyacğım için alt tire koydum.
# kodun yavaş olmasını engeller.
while camera.isOpened():
    _, frame = camera.read()
    
    # okudğum resmi HSV'ye dönüştürme
    # frame bizim resmimiz.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
   
    # 2'ye bölme sebebi opencv de 180 değerini kullanıyor
    # değerleri okuyoruz.
    H1 = int(cv2.getTrackbarPos("H1", "frame") / 2)
    H2 = int(cv2.getTrackbarPos("H2", "frame") / 2)
    S1 = cv2.getTrackbarPos("S1", "frame")
    S2 = cv2.getTrackbarPos("S2", "frame")
    V1 = cv2.getTrackbarPos("V1", "frame")
    V2 = cv2.getTrackbarPos("V2", "frame")
    
    # bir nesneyi tespit etmek için kullandık, renkleri yakalamak için.
    lower = np.array([H1, S1, V1]) # tek tek h s v ye tekabül eder
    upper = np.array([H2, S2, V2])
    
    # opencv kütüphanesinde renk değerleri en fazla 180'ne kadar ayarlanmış
    mask = cv2.inRange(hsv, lower, upper)
    
    # bunu yaptığım zaman görüntüyü renkli de görebileceğim
    # hangi renkleri geçirdiğim belli olur.
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow("frame", frame)
    cv2.imshow("hsv", mask)
    cv2.imshow("res", res)
    
    if cv2.waitKey(5) == ord("q"):
        break
        
cv2.destroyAllWindows()


