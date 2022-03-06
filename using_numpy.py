import cv2
import numpy as np

img = np.zeros([512, 512, 3], np.uint8)
print(img)

# to fill the background part or change the color from black to ur choice color
img[:] = 135, 50, 81

# to draw line
# if u don't know the h & w then use this ->(img.shape[1], img.shape[0]) for diagonal line
img = cv2.line(img, (0, 0), (255, 255), (210, 172, 230), 10)

img = cv2.arrowedLine(img, (0, 255), (255, 255), (212, 184, 207), 10)

img = cv2.rectangle(img, (384, 0), (512, 128), (171, 132, 164), 10)  # here u can use cv2.filled or thickness in nos

img = cv2.circle(img, (447, 63), 63, (210, 172, 230), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'COLOUR', (10, 500), font, 4, (222, 16, 122), 10, cv2.LINE_AA)

cv2.imshow('colourful', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
