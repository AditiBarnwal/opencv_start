import cv2

path = '_png images - Google Search.png'

img = cv2.imread(path)

imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original", img)
cv2.imshow("HSV", imghsv)

cv2.waitKey(0)
