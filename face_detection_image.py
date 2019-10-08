import cv2
import numpy as np

# Defining the classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#  Read the input image
img = cv2.imread('promo.jpg')

# Resize image just for convenience
img = cv2.resize(img, (1480, 840))

# Transform image to gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# adding text
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'height: ' + str(img.shape[0]) + '   width: ' + str(img.shape[1])
img = cv2.putText(img, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

# Display the output
cv2.imshow('img', img)
# Save file (optional)
cv2.imwrite('saved.jpg',img)


cv2.waitKey()
cv2.destroyAllWindows

