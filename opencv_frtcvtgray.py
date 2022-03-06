import cv2

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(0)

while True:
    # Capture frame by frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame.
    cv2.imshow('Its front view', gray)

    # Press Q to exit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release
# the video capture object
cap.release()
cv2.destroyAllWindows()
