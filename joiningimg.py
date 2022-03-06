import cv2
import numpy as np

img = cv2.imread('baboon.jpg')

imghor = np.hstack((img, img))  # horizontal stack
imgver = np.vstack((img, img))  # vertical stack

cv2.imshow("image", img)
cv2.imshow("horizontal stack", imghor)
cv2.imshow("vertical stack", imgver)

cv2.waitKey(0)
cv2.destroyAllWindows()
