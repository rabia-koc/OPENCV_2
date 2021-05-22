import cv2
import numpy as np

img = cv2.imread("1.jpeg")

rows, cols = img.shape[:2]

src_points = np.float32([
    [80, 100], 
    [400, 90],
    [50, 400],
    [400, 400]])

dst_points = np.float32([
    [0, 0], 
    [cols -1, 0],
    [0, rows -1],
    [cols -1, rows -1]])

projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

img_output = cv2.warpPerspective(img, projective_matrix, (cols, rows))

cv2.imshow("img", img)
cv2.imshow("img_output", img_output)

cv2.waitKey()
cv2.destroyAllWindows()
