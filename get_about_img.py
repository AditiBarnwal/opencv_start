import cv2
import numpy as np

img = cv2.imread('_png images - Google Search.png')

print(img.shape)  # return a tuple of number of rows ,column, column
print(img.size)   # return total number of pixels is added
print(img.dtype)  # return image datatype is obtained

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()