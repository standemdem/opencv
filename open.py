import numpy as np
import cv2

#  Access the camera
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter('output.avi', fourcc, 20, (width, height))

print(width, height, fps)

# start the cam in an indefinite while loop
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        # get width and height
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #  print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        # change cam color to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('Camera', gray)

    # stop capture if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows
