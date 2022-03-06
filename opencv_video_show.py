import cv2

# cap = cv2.VideoCapture(anything like string, mix nos, except 0,1)
# >> return false
cap = cv2.VideoCapture(0)

print(cap.isOpened())
# Read until video is completed.
while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('Its front view', frame)

    # Press Q to exit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
