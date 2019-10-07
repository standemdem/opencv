import numpy as np
import cv2

#  Access the camera
cap = cv2.VideoCapture(0)

# Get width, height and frame per second
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Set some values for width (3)
cap.set(3, 640)
# Set some values for height (4)
cap.set(4, 480)

print(cap.get(3), cap.get(4))
# start the cam in an indefinite while loop
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:

        # change cam color to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('Camera', gray)

    # stop capture if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows
