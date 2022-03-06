import cv2
import numpy as np


def mousePoints(event, x, y, flags, params):
    # In the user - defined function,
    # check for left mouse clicks using the cv2.EVENT_LBUTTONDOWN attribute.
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)


img = cv2.imread("butterfly.jpg")
cv2.imshow("Butterfly", img)

# Call the cv2.setMouseCallback() function and pass the image window
# and the user-defined function as parameters.
cv2.setMouseCallback("Butterfly", mousePoints)

cv2.waitKey(0)

# Display the coordinates on the Shell.
# Display the coordinates on the created window.
# Do the same for right mouse clicks using the cv2.EVENT_RBUTTONDOWN attribute.
# Change the color while displaying the coordinates on the image to distinguish from left clicks.
