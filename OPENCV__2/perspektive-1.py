
# 4 nokta 4 köşe seçtim

import cv2
import numpy as np

img = cv2.imread("1.jpeg")

rows, cols = img.shape[:2]

src_points = np.float32([
    [0, 0], 
    [cols -1, 0],
    [0, rows -1],
    [cols -1, rows -1]])
# 1.si üst sol
# 2.si üst sağ
# 3.sü alt sol
# 4.sü alt sağ

dst_points = np.float32([
    [0 ,0],
    [cols -1, 0],
    [int(0.33 * (cols -1)), rows -1],
    [int(0.66 * (cols -1)), rows -1]])


projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

img_output = cv2.warpPerspective(img, projective_matrix, (cols, rows))

cv2.imshow("img", img)
cv2.imshow("img_output", img_output)

cv2.waitKey()
cv2.destroyAllWindows()

