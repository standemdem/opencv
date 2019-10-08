import cv2

# Read the input image
img = cv2.imread('lenna.png')

# Display the output
cv2.imshow('img', img)
cv2.waitKey()