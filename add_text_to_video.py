import numpy as np
import cv2
import datetime

#  Access the camera
cap = cv2.VideoCapture(0)

# Set some values for width (3)
cap.set(3, 640)
# Set some values for height (4)
cap.set(4, 480)

print(cap.get(3), cap.get(4))

# start the cam in an indefinite while loop
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        # picking font
        font = cv2.FONT_HERSHEY_SIMPLEX

        # creating text
        date_str = str(datetime.datetime.today())
        text = 'width: ' + str(cap.get(3))+ '   height: ' + str(cap.get(4)) + ' ' + date_str
        # adding text
        cv2.putText(frame, text, (10, 50), font, 1, (0, 255,255), 2, cv2.LINE_AA)

        # Display the resulting frame
        cv2.imshow('Camera', frame)

    # stop capture if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows
