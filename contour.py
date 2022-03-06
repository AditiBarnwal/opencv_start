import cv2
import numpy as np

img = cv2.imread('shapes.png')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
print(img)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)
cv2.imshow('image', img)
cv2.imshow('Gray image ', imgGray)

cv2.imshow('image Blur', imgBlur)
cv2.imshow('contour', imgCanny)
cv2.waitKey(0)
