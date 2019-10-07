import cv2
import numpy as np

# Create an img with numpy using np.zeros
# img = np.zeros([512, 512,3], np.uint8)

# import the image
img = cv2.imread('Lenna.png')

# create a line(image, start point, stop point, color, thickness)
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5 )

# create an arrowed line(image, start point, stop point, color, thickness)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5 )

# create a rectangle(image, top left corner, bottom right corner, color, thickness)
img = cv2.rectangle(img, (304, 0), (510, 128), (0, 0, 255), 5)

# create a circle(image, center, radius, color, thickness)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), 5)

# add text to an image (img, text, startpoint, font, fontsize, color, thickness, ??)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (255, 255, 0), 5, cv2.LINE_AA)

# display image
cv2.imshow('image', img)

# kill program when pressing any key
cv2.waitKey(0)
cv2.destroyAllWindows()