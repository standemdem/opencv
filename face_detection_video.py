import cv2

# Defining the classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


cv2.waitKey()
cv2.destroyAllWindows