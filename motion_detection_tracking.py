import cv2

cap = cv2.VideoCapture(0)

# declaring 2 frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    # calculating the absolute difference between first and second frames
    diff = cv2.absdiff(frame1, frame2)

    # easier to find contours when it's gray
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    dilated = cv2.dilate(thresh, None, iterations=3)

    _, contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)


    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour)  < 9500:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2)
        text = 'Status: {}'.format('movement')
        cv2.putText(frame1, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3 )
    cv2.imshow('test', frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    # stop capture if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
