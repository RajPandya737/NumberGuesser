import cv2
import numpy

img = cv2.imread("Numbers/3.png", 0)

print(img)

cv2.imwrite("test3.png", img)

